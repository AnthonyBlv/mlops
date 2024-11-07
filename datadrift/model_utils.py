import joblib
import pandas as pd
from eurybia import SmartDrift

PATH = 'regression.joblib'

def load_model():
    model = joblib.load(PATH)
    return model

def predict(model, input):
    input = pd.DataFrame([input], columns=['size', 'nb_rooms', 'garden'])
    return model.predict(input)

def data_drift(df_train, df_prod):
    sd = SmartDrift(
        df_current=df_prod,
        df_baseline=df_train)

    sd.compile()
    return sd.auc
    