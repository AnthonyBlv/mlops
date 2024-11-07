from fastapi import FastAPI
import model_utils
import pandas as pd

app = FastAPI()
df_baseline = pd.read_csv("houses.csv")
df_baseline = df_baseline.drop(columns=['price','orientation'])
df_prod = pd.DataFrame(data=[],columns=df_baseline.columns)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(input: dict):
    global df_prod
    input = [input["size"], input["nb_rooms"], input["garden"]]
    input = pd.DataFrame([input], columns=['size', 'nb_rooms', 'garden'])
    df_prod = pd.concat([df_prod, input])
    print(df_prod.shape)
    print('lol')
    model = model_utils.load_model()
    out = model_utils.predict(model, input)
    return {"price": out[0]}


@app.post("/detect-drift")
def detect_datadrift():
    global df_baseline, df_prod
    drift = model_utils.data_drift(df_baseline, df_prod)
    if drift > 0.8:
        return {"drift": drift, "alert": "Data drift detected"}
    else: 
        return {"drift": drift, "alert": "No data drift detected"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)