# model_logic.py
import pandas as pd
import numpy as np
import joblib

# Load saved models and objects
lin_model = joblib.load("linear_model.pkl")
xgb_model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")
input_columns = joblib.load("input_columns.pkl")

def preprocess_input(user_input):
    df = pd.DataFrame([user_input])
    df = pd.get_dummies(df)

    # Ensure all required columns are present
    for col in input_columns:
        if col not in df.columns:
            df[col] = 0  # add missing columns with 0

    df = df[input_columns]  # reorder columns
    df_scaled = scaler.transform(df)
    return df_scaled

def predict_price(model, processed_input):
    return model.predict(processed_input)[0]
