import joblib
from eurybia import SmartDrift
from eurybia import SmartDrift

PATH = 'regression.joblib'

def load_model():
    model = joblib.load(PATH)
    return model

def predict(model, input):
    return model.predict(input)

def data_drift(df_train, df_prod):
    sd = SmartDrift(
        df_current=df_prod,
        df_baseline=df_train)

    sd.compile()
    return sd.auc
    