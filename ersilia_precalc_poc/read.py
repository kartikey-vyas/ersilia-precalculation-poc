import pandera as pa
from pandera.typing import DataFrame

from ersilia_precalc_poc.models import Prediction, PredictionSchema

# def read_predictions_from_s3(model_id: str, s3_config:) -> DataFrame[PredictionSchema]


@pa.check_types
def get_predictions_from_dataframe(model_id: str, prediction_df: DataFrame[PredictionSchema]) -> list[Prediction]:
    """Converts a valid pandas dataframe of predictions into a list of prediction objects

    Args:
        model_id (str): ID of the model which generated the predictions
        prediction_df (DataFrame[PredictionSchema]): Validated pandas dataframe containing predictions

    Returns:
        list[Prediction]: list of prediction objects
    """
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
