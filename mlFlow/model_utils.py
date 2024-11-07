import mlflow
import mlflow.pyfunc
import numpy as np

def load_model(version):
    mlflow.set_tracking_uri(uri="http://localhost:8080")
    name = "models:/tracking-quickstart/"+str(version)
    loaded_model = mlflow.sklearn.load_model(name)
    return loaded_model


def predict(model, input):
    input = np.array(input)
    input = np.expand_dims(input, axis=0)
    return model.predict(input)