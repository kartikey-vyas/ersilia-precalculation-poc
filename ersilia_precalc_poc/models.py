from pydantic import BaseModel


class Prediction(BaseModel):
    """Dataclass to represent a single prediction"""

    model_id: str
    input_key: str
    smiles: str
    output: float
