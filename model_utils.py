import joblib
import pandas as pd

PATH = 'regression.joblib'

def load_model():
    model = joblib.load(PATH)
    return model

def predict(model, input):
    input = pd.DataFrame([input], columns=['size', 'nb_rooms', 'garden'])
    return model.predict(input)