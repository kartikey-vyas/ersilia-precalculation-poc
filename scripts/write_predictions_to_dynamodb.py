import sys
import time

import boto3
import pandas as pd

from ersilia_precalc_poc.read import get_predictions_from_dataframe
from ersilia_precalc_poc.write import write_precalcs_batch_writer

# aws region: eu-central-1
# dynamodb table name: precalculations-poc

test_data = [
    {
        "model_id": "examplemodel",
        "input_key": "PCQFQFRJSWBMEL-UHFFFAOYSA-N",
        "smiles": "COC(=O)C1=CC=CC2=C1C(=O)C1=CC([N+](=O)[O-])=CC=C21",
        "output": "283.239",
    },
    {
        "model_id": "examplemodel",
        "input_key": "MRSBJIAZTHGJAP-UHFFFAOYSA-N",
        "smiles": "CN(C)CCC1=CN(C)C2=CC=C(O)C=C12",
        "output": "218.3",
    },
]

DYNAMODB_TABLE_NAME = "precalculations-poc"

if __name__ == "__main__":
    # todo: use argparse
    cli_choice = sys.argv[1]

    # default test fixture, just chuck some records into the table
    if sys.argv[1] == "test":
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table(DYNAMODB_TABLE_NAME)
        data = test_data

        with table.batch_writer() as writer:
            for item in data:
                writer.put_item(
                    Item={
                        "PK": f"INPUTKEY#{item['input_key']}",
                        "SK": f"MODELID#{item['model_id']}",
                        "Smiles": item["smiles"],
                        "Precalculation": item["output"],
                        "Timestamp": str(time.time()),
                    }
                )
    else:
        # look for csv at provided path
        df = pd.read_csv(cli_choice)

        print(f"read {len(df)} predictions from {cli_choice}")

        pred_data = get_predictions_from_dataframe("examplemodel", df)

        write_precalcs_batch_writer(DYNAMODB_TABLE_NAME, pred_data)
