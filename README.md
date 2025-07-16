# 🚗 Car Price Prediction App

A Streamlit-based web app that predicts the price of a car using machine learning models like **Linear Regression** and **XGBoost**. Built to showcase how simple ML tools can solve real-world problems.

---
<img width="1920" height="2171" alt="chrome-capture-2025-6-17" src="https://github.com/user-attachments/assets/411e91b5-5315-404b-954f-53ad8d88af60" />

## 🔍 Features

- Upload your car dataset (CSV)
- Train and evaluate ML models
- Predict car price based on user inputs
- Interactive interface with Streamlit

---

## 🧠 Models Used

- Linear Regression
- XGBoost Regressor

---

## 🔢 Key Features Considered

- Year
- Kilometers Driven
- Engine Size
- Mileage
- Seats
- Brand
- Model
- Fuel Type
- Transmission
- Owner Type
- City
- Color
- Insurance

---

## 🚀 Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/MrCoss/Car_Price_Prediction_App.git
cd Car_Price_Prediction_App
````

2. **Set up the environment:**

```bash
python -m venv venv
venv\Scripts\activate     # On Windows
pip install -r requirements.txt
```

3. **Launch the app:**

```bash
streamlit run app.py
```

---

## 🧾 File Structure

```
Car_Price_Prediction_App/
│
├── app.py              # Streamlit app
├── train.py            # Model training script
├── model_logic.py      # ML processing and prediction functions
├── sample_data.csv     # Sample synthetic dataset (optional)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🙌 Contributions

Contributions are welcome!
Feel free to fork the project, add features, or fix bugs and submit a pull request.

---

## 👨‍💻 Author

Made by **Costas Pinto**
GitHub: [@MrCoss](https://github.com/MrCoss)
