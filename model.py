#import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle


def train_model(data):
    # Verileri bir Pandas DataFrame'ine yükleyin
    data = pd.read_csv(data)

    # Bağımlı ve bağımsız değişkenleri tanımlayın
    X = data.drop("Marks", axis=1)
    y = data["Marks"]

    # Modeli eğitin
    model = LinearRegression()
    model.fit(X, y)

    # Modeli kaydedin
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

if __name__ == "__main__":
    data_path = "student.csv"
    train_model(data_path)