from pydantic import BaseModel

class SentimentResult(BaseModel):
    text: str
    label: str
    score: float
