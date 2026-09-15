# Traffic Volume Prediction using Python + Scikit-learn

## Project Overview
This machine learning project predicts the expected traffic volume using time, weather, and holiday information.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Random Forest Regressor
- Matplotlib
- Joblib

## Input Features
- Hour
- Day of week
- Temperature in Celsius
- Rainfall in millimeters
- Holiday indicator

## Output
Predicted number of vehicles.

## How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Train the model
```bash
python train_model.py
```

This creates:
- `traffic_volume_model.pkl`
- `feature_importance.png`

### 3. Predict traffic volume
```bash
python predict.py
```

Enter the requested traffic and weather details.

## Dataset
The included dataset is synthetic and intended for educational demonstration.

## Important Note
For real traffic planning, use validated traffic sensor data and account for road conditions, accidents, events, and local traffic patterns.
