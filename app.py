import streamlit as st
from model_logic import preprocess_input, predict_price, lin_model, xgb_model

st.set_page_config(page_title="Car Price Prediction", layout="centered")
st.title("🚘 Car Price Prediction App")
st.write("Fill in car details below to predict its price using Machine Learning models.")

# --- Car Info Inputs ---
st.header("Enter Car Details")
user_input = {}

user_input["Year"] = st.number_input("📅 Year", min_value=2000, max_value=2025, value=2015)
user_input["Kilometers_Driven"] = st.number_input("🛣️ Kilometers Driven", min_value=0, value=50000)
user_input["Engine_Size"] = st.number_input("🧱 Engine Size (cc)", min_value=600, value=1200)
user_input["Mileage"] = st.number_input("⚙️ Mileage (kmpl)", min_value=5.0, max_value=50.0, value=18.0)
user_input["Seats"] = st.selectbox("💺 Seats", [4, 5, 6, 7])

user_input["Brand"] = st.selectbox("🚗 Brand", ["Maruti", "Hyundai", "Toyota", "Honda", "Ford", "BMW"])
user_input["Model"] = st.selectbox("🧾 Model", ["Swift", "Alto", "Baleno", "City", "Amaze", "i10", "i20", "Creta", "EcoSport", "Figo", "Fortuner", "Innova", "X1"])
user_input["Fuel_Type"] = st.selectbox("⛽ Fuel Type", ["Petrol", "Diesel", "CNG", "Electric"])
user_input["Transmission"] = st.selectbox("🔀 Transmission", ["Manual", "Automatic"])
user_input["Owner"] = st.selectbox("👤 Owner", ["First", "Second", "Third"])
user_input["City"] = st.selectbox("🌆 City", ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"])
user_input["Color"] = st.selectbox("🎨 Color", ["White", "Black", "Silver", "Red", "Blue"])
user_input["Insurance_Status"] = st.selectbox("🛡️ Insurance", ["Yes", "No"])

# --- Input Validation ---
if user_input["Kilometers_Driven"] > 1_000_000:
    st.warning("⚠️ Too many kilometers! Clipped to 1,000,000.")
    user_input["Kilometers_Driven"] = 1_000_000

if user_input["Mileage"] < 5 or user_input["Mileage"] > 50:
    st.warning("⚠️ Unusual mileage. Set to average (18 kmpl).")
    user_input["Mileage"] = 18.0

# --- Predict Prices ---
if st.button("🔍 Predict Car Price"):
    try:
        processed = preprocess_input(user_input)

        price_lin = max(0, predict_price(lin_model, processed))  # No negative prices
        price_xgb = max(0, predict_price(xgb_model, processed))

        st.success(f"💰 Linear Regression Price: ₹{round(price_lin):,}")
        st.success(f"🚀 XGBoost Price: ₹{round(price_xgb):,}")
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
