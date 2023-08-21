import json
import logging
import time
from decimal import Decimal
from typing import List

import boto3
import pandas as pd

from ersilia_precalc_poc.models import Prediction


logger = logging.Logger("DynamoDBWriter")


def format_precalcs_for_dynamodb(precalcs: List[Prediction]):
    pass


# here are a few different ways we could write a large number of predictions to dynamodb
def write_precalcs_batch_writer(dynamodb_table: str, precalcs: List[Prediction]):
    # todo: timestamp/versioning for predictions written to dynamo

    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(dynamodb_table)

    with table.batch_writer() as writer:
        for item in precalcs:
            writer.put_item(
                Item={
                    "PK": f"MODELID#{item.model_id}",
                    "SK": f"INPUTKEY#{item.input_key}",
                    "Smiles": item.smiles,
                    "Precalculation": json.loads(
                        json.dumps(item.output), parse_float=Decimal
                    ),
                    "Timestamp": str(time.time()),
                }
            )


def write_precalcs_manual_batching(dynamodb_table: str, precalcs: List[Prediction]):
    # dynamodb = boto3.client("dynamodb")
    print("unimplemented")
    pass


def predictions_from_dataframe(
    model_id: str, prediction_df: pd.DataFrame
) -> List[Prediction]:
    predictions = prediction_df.to_dict("records")

    return [
        Prediction(
            model_id=model_id,
            input_key=prediction["key"],
            smiles=prediction["input"],
            output=prediction["mw"],
        )
        for prediction in predictions
    ]
