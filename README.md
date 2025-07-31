 # Car Price Prediction Web Application

[![Status: Active](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://shields.io/)
[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![Framework: Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)](https://streamlit.io/)
[![Models: Scikit-learn & XGBoost](https://img.shields.io/badge/Models-Sklearn%20%26%20XGBoost-orange)](https://scikit-learn.org/)

A user-friendly web application built with **Streamlit** that predicts the resale value of used cars. This project leverages machine learning models like **Linear Regression** and **XGBoost** to provide accurate price estimates based on user-provided car features.

---
<img width="1920" height="2171" alt="App Screenshot" src="https://github.com/user-attachments/assets/411e91b5-5315-404b-954f-53ad8d88af60" />

---

## 📖 Table of Contents
- [1. Project Overview & Business Value](#1-project-overview--business-value)
- [2. Features & Functionality](#2-features--functionality)
- [3. Technical Workflow](#3-technical-workflow)
- [4. Machine Learning Models](#4-machine-learning-models)
- [5. File Structure Explained](#5-file-structure-explained)
- [6. Technical Stack](#6-technical-stack)
- [7. How to Run Locally](#7-how-to-run-locally)
- [8. Contributions](#8-contributions)
- [9. Author](#9-author)

---

## 1. Project Overview & Business Value

The used car market is complex, with prices fluctuating based on numerous factors like brand, age, mileage, and condition. For both buyers and sellers, determining a fair market price can be challenging.

This project aims to solve this problem by providing an accessible tool for instant car price prediction. By inputting key vehicle attributes, users can get a data-driven price estimate, empowering them to make informed decisions.

- **For Sellers:** Helps in setting a competitive and realistic asking price.
- **For Buyers:** Provides a benchmark to evaluate listings and negotiate effectively.
- **For Dealerships:** Can be used to quickly appraise vehicles for trade-ins or purchases.

---

## 2. Features & Functionality

The application is designed to be interactive and intuitive:

- **Dynamic Data Upload:** Users can upload their own car dataset in CSV format. The app will automatically train models on this new data.
- **Interactive Prediction Form:** A clean sidebar form allows users to input car features (e.g., Year, Brand, Fuel Type, Kilometers Driven) to get a price prediction.
- **Dual Model Approach:** The app trains both a simple Linear Regression model (as a baseline) and a powerful XGBoost Regressor for more accurate predictions.
- **Real-Time Results:** Predictions are generated and displayed instantly upon user input.
- **User-Friendly Interface:** Built with Streamlit for a seamless and responsive web experience.

---

## 3. Technical Workflow

The application follows a standard machine learning pipeline:

1.  **Data Loading & Caching:** The app loads the provided CSV data. Streamlit's caching is used to avoid reloading data on every interaction, ensuring a fast user experience.
2.  **Data Preprocessing:**
    - The `model_logic.py` script handles data cleaning (handling missing values) and feature engineering.
    - Categorical features (like Brand, Model, Fuel Type) are transformed into a numerical format using One-Hot Encoding.
3.  **Model Training:**
    - The `train.py` script splits the data into training and testing sets.
    - It then trains both the Linear Regression and XGBoost models on the training data.
4.  **Prediction:**
    - User inputs from the Streamlit sidebar are collected into a DataFrame.
    - This input data is preprocessed using the same steps as the training data.
    - The trained models then predict the price based on the processed inputs.
5.  **Display:** The predicted price is displayed clearly in the main panel of the web app.

---

## 4. Machine Learning Models

Two regression models are implemented to provide a comprehensive analysis:

-   **Linear Regression:** A simple, interpretable model that serves as a solid baseline. It helps to understand the linear relationships between the car's features and its price.
-   **XGBoost Regressor (Extreme Gradient Boosting):** A sophisticated and powerful gradient boosting algorithm known for its high performance and accuracy. It can capture complex, non-linear patterns in the data, typically resulting in more precise predictions.

---

## 5. File Structure Explained

The project is organized into modular scripts for clarity and maintainability:

```

Car\_Price\_Prediction\_App/
│
├── app.py              \# Main Streamlit script. Defines the UI and orchestrates the workflow.
├── train.py            \# Contains the logic for training the ML models.
├── model\_logic.py      \# Handles data preprocessing, feature engineering, and prediction functions.
├── sample\_data.csv     \# A sample dataset to demonstrate the app's functionality out-of-the-box.
├── requirements.txt    \# Lists all Python dependencies required to run the project.
└── README.md           \# This documentation file.

````

---

## 6. Technical Stack

-   **Backend & ML:** Python
-   **Web Framework:** Streamlit
-   **Machine Learning:** Scikit-learn, XGBoost
-   **Data Manipulation:** Pandas, NumPy

---

## 7. How to Run Locally

Follow these steps to set up and run the application on your local machine.

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/MrCoss/Car_Price_Prediction_App.git](https://github.com/MrCoss/Car_Price_Prediction_App.git)
    cd Car_Price_Prediction_App
    ```

2.  **Create and Activate a Virtual Environment:** (Recommended)
    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate it (on Windows)
    .\venv\Scripts\activate

    # Activate it (on macOS/Linux)
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch the Streamlit App:**
    ```bash
    streamlit run app.py
    ```
    Your web browser should automatically open with the running application.

---

## 8. Contributions

Contributions are highly welcome! If you have ideas for new features, find a bug, or want to improve the code, please feel free to:
1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeatureName`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeatureName`).
6.  Open a Pull Request.

---

## 9. Author
This project was created by **Costas Pinto**.

- **GitHub:** [@MrCoss](https://github.com/MrCoss)
