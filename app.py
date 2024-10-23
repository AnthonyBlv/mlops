from typing import Union
from fastapi import FastAPI
import model_utils
import pandas as pd

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(input: dict):
    input = [input["size"], input["nb_rooms"], input["garden"]]
    model = model_utils.load_model()
    out = model_utils.predict(model, input)
    return {"price": out[0]}