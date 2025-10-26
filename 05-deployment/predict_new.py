import pickle
import uvicorn

from fastapi import FastAPI
from typing import Dict, Any

from typing import Literal
from pydantic import BaseModel, Field
from pydantic import ConfigDict

class Customer(BaseModel):
    model_config = ConfigDict(extra="forbid")
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    tenure: int = Field(..., ge=0)
    monthlycharges: float = Field(..., ge=0.0)
    totalcharges: float = Field(..., ge=0.0)


class PredictResponse(BaseModel):
    churn_probability: float
    churn: bool

app = FastAPI(title="Churn-Prediction")


with open('model.bin', 'rb') as f_in:
    model = pickle.load(f_in)
    


def predict_single(model, datapoint):
    churn = model.predict_proba(datapoint)[0, 1]
    return float(churn)

@app.post("/predict")
def predict(datapoint: Customer) -> PredictResponse:
    churn_probability = predict_single(model, datapoint.model_dump())

    return PredictResponse(
        churn_probability=churn_probability,
        churn=bool(churn_probability >= 0.5)
    )



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)
