import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load enhanced dataset
df = pd.read_csv("enhanced_car_data.csv").dropna()

# Target variable
y = df["Price"]

# Drop target from features
X = df.drop("Price", axis=1)

# One-hot encode categorical features
categorical_cols = X.select_dtypes(include=["object"]).columns
X = pd.get_dummies(X, columns=categorical_cols, drop_first=True)

# Scale numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Train models
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

xgb_model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5)
xgb_model.fit(X_train, y_train)

# Save models and transformers
joblib.dump(lin_model, "linear_model.pkl")
joblib.dump(xgb_model, "xgb_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(X.columns.tolist(), "input_columns.pkl")

# Evaluate function
def evaluate(model, name):
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    print(f"\n📊 {name} Evaluation:")
    print(f"  - MSE: {mse:.2f}")
    print(f"  - R² Score: {r2:.4f}")

# Show performance
evaluate(lin_model, "Linear Regression")
evaluate(xgb_model, "XGBoost")

# Show features used
print("\n🧾 Features used for training (in order):")
for i, col in enumerate(X.columns.tolist(), 1):
    print(f"{i}. {col}")
