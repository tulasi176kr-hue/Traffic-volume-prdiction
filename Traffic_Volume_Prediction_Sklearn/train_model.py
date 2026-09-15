import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "traffic_volume.csv"
MODEL_PATH = BASE_DIR / "traffic_volume_model.pkl"
CHART_PATH = BASE_DIR / "feature_importance.png"

df = pd.read_csv(DATA_PATH)

features = ["hour", "day_of_week", "temperature_c", "rain_mm", "holiday"]
target = "traffic_volume"

X = df[features]
y = df[target]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(
    n_estimators=150, random_state=42, max_depth=10
)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
rmse = mean_squared_error(y_test, predictions) ** 0.5
r2 = r2_score(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f}")
print(f"Root Mean Squared Error: {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

joblib.dump(model, MODEL_PATH)
print(f"Model saved to: {MODEL_PATH}")

importance = pd.Series(model.feature_importances_, index=features).sort_values()
importance.plot(kind="barh", figsize=(9, 5), title="Traffic Volume Feature Importance")
plt.tight_layout()
plt.savefig(CHART_PATH)
print(f"Chart saved to: {CHART_PATH}")
