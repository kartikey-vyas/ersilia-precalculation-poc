from ersilia_precalc_poc.models import Prediction


def test_prediction():
    fixture = {"model_id": "a", "input_key": "b", "smiles": "C", "output": 1.0}

    pred = Prediction(**fixture)

    assert isinstance(pred, Prediction)
