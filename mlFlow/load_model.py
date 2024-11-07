import mlflow
import mlflow.pyfunc
import pandas as pd
import sklearn.datasets as datasets


# Load the model
mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

loaded_model = mlflow.sklearn.load_model("models:/tracking-quickstart/7")

# Load the Iris dataset
X, y = datasets.load_iris(return_X_y=True)
X_test = [X[0]]
y_test = y[0]
print(X[0])

# Predict on the test set
predictions = loaded_model.predict(X_test)
print(predictions)
