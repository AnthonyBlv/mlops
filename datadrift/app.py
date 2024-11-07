from fastapi import FastAPI
from sklearn.model_selection import train_test_split
import model_utils
import pandas as pd
from eurybia import SmartDrift


app = FastAPI()
df = pd.read_csv('houses.csv')
df_train, df_prod = train_test_split(df, test_size=0.5, random_state=42)
df_aberrant = df_train.copy()

df_aberrant['price'] = df_aberrant['price'] * 10  # Augmenter considérablement le prix
df_aberrant['size'] = df_aberrant['size'] / 5  # Réduire la surface
df_aberrant['nb_rooms'] = df_aberrant['nb_rooms'] + 20  # Augmenter le nombre de chambres

# Vérifier si Eurybia détecte les données aberrantes
sd_aberrant = SmartDrift(
  df_current=df_aberrant,
  df_baseline=df_train)

sd_aberrant.compile()

drift = sd_aberrant.auc

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/predict")
def predict(input: dict):
    input = [input["size"], input["nb_rooms"], input["garden"]]
    model = model_utils.load_model()
    out = model_utils.predict(model, input)
    return {"price": out[0]}

@app.post("/detect-drift")
def detect_datadrift():
    if drift > 0.8:
        return {"drift": drift, "alert": "Data drift detected"}
    else: 
        return {"drift": drift, "alert": "No data drift detected"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)