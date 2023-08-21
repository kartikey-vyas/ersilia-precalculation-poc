from ersilia_precalc_poc.models import Prediction


def test_prediction():
    fixture = {"model_id": "a", "input_key": "b", "smiles": "C", "output": 1}

    prediction = Prediction(model_id="a", input_key="b", smiles="C", output=1)

    constructed_pred = Prediction.model_construct(**fixture)

    assert prediction.model_dump() == fixture
    assert constructed_pred == prediction
