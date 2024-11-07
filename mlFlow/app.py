from typing import Union
from fastapi import FastAPI
import model_utils

app = FastAPI()
version = 7

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(input: dict):
    input = input["data"]
    model = model_utils.load_model(version)
    out = model_utils.predict(model, input)
    print(out)
    return {"prediction": int(out[0])}

@app.post("/update-model")
def update_model(input: dict):
    version = input[version]

