# How to Run: Traffic Volume Prediction using Python + Scikit-learn

This machine learning project predicts the expected traffic volume using time, weather, and holiday information.

---

## 1. Prerequisites

- **Python**: Python 3.9+ (Python 3.14 tested)
- **Terminal**: Windows PowerShell, Command Prompt, or VS Code integrated terminal
- **Dependencies**: `pandas`, `scikit-learn`, `numpy`, `joblib`, `matplotlib`

---

## 2. Open Terminal & Navigate to Project Directory

Open PowerShell or Command Prompt, then change directory to the project folder:

```powershell
# Note: Project files are inside the nested "Traffic_Volume_Prediction_Sklearn" folder:
cd "c:\Users\user\Desktop\jj college\Traffic_Volume_Prediction_Sklearn\Traffic_Volume_Prediction_Sklearn"
```

---

## 3. Install Dependencies

Install required packages:

```powershell
pip install -r requirements.txt
```

> **Windows Note**: If `python` or `pip` opens the Microsoft Store, specify the direct Python path:
> ```powershell
> & "C:\Users\user\AppData\Local\Python\bin\python.exe" -m pip install -r requirements.txt
> ```

---

## 4. Step 1: Train the Machine Learning Model

Execute the training script to train and save the model:

```powershell
python train_model.py
```
*(or `py train_model.py` / `& "C:\Users\user\AppData\Local\Python\bin\python.exe" train_model.py`)*

### What this does:
1. Loads the dataset from `data/traffic_volume.csv`.
2. Trains a **RandomForestRegressor** model predicting `traffic_volume`.
3. Evaluates model performance (Mean Absolute Error, Mean Squared Error, R2 Score).
4. Saves the trained model (`.pkl` file).
5. Generates and saves visualization plots/charts (e.g., feature importance or segment visualizations).

---

## 5. Step 2: Run Predictions

Run the prediction script to test predictions:

```powershell
python predict.py
```

### Interactive Inputs:
This script prompts for inputs in the terminal. Here is an example of what to enter when prompted:

| Prompt / Field | Example Value |
| :--- | :--- |
| `Hour (0-23` | `14` |
| `Day of week (0=Monday, 6=Sunday` | `2` |
| `Temperature in Celsius:` | `24.5` |
| `Rain in mm:` | `0.0` |
| `Holiday? (1=Yes, 0=No` | `1` |

---

## 6. Directory Structure

```text
Traffic_Volume_Prediction_Sklearn/
├── data/
│   └── traffic_volume.csv
├── predict.py
├── train_model.py
├── requirements.txt
├── README.md
└── HOW_TO_RUN.md
```
