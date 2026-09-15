import joblib
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "traffic_volume_model.pkl"

model = joblib.load(MODEL_PATH)

print("Traffic Volume Prediction")
print("-" * 35)

hour = int(input("Hour (0-23): "))
day_of_week = int(input("Day of week (0=Monday, 6=Sunday): "))
temperature = float(input("Temperature in Celsius: "))
rain = float(input("Rain in mm: "))
holiday = int(input("Holiday? (1=Yes, 0=No): "))

sample = pd.DataFrame([{
    "hour": hour,
    "day_of_week": day_of_week,
    "temperature_c": temperature,
    "rain_mm": rain,
    "holiday": holiday
}])

prediction = model.predict(sample)[0]
print(f"\nPredicted Traffic Volume: {prediction:.0f} vehicles")
