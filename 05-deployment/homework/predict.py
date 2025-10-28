import pickle
import uvicorn

from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI(title="Lead-Scoring")

with open('pipeline_v2.bin', 'rb') as file:
    pipeline = pickle.load(file)


@app.post("/predict")
def predict(input_data: Dict[str, Any]):
    lead_proba = pipeline.predict_proba(input_data)[0, 1]
    return {
        "lead_proba": float(lead_proba)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)