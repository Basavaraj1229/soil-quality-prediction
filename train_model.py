import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("soil_dataset.csv")
X = data.drop("soil_type", axis=1)
y = data["soil_type"]

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

joblib.dump(model, "soil_model.pkl")
