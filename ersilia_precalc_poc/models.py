from dataclasses import dataclass


@dataclass
class Prediction:
    """Dataclass to represent a single prediction"""

    model_id: str
    input_key: str
    smiles: str
    output: float