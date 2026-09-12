# Traffic-volume-prdiction
Traffic Volume Prediction is a machine learning project that predicts road traffic using time, weather, rainfall, and holiday data. It uses a Random Forest Regressor and provides predictions through Python and a Streamlit web app.
# Traffic Volume Prediction Using Scikit-learn

## Project Overview

Traffic Volume Prediction is a machine learning project designed to estimate the number of vehicles travelling on a road during a particular time period.

The project uses historical traffic and environmental information to train a machine learning model. The model predicts traffic volume based on time, weather conditions, and holiday information.

A Random Forest Regressor algorithm from Scikit-learn is used for prediction.

## Objectives

* Predict the expected traffic volume.
* Analyze the factors that influence traffic flow.
* Use machine learning for traffic volume estimation.
* Provide an easy-to-use prediction interface.
* Display feature importance and traffic trends.
* Help understand traffic conditions under different scenarios.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Random Forest Regressor
* Matplotlib
* Joblib
* Streamlit

## Input Features

The model uses the following five features:

1. **Hour** – Hour of the day from 0 to 23.
2. **Day of Week** – Day represented from 0 to 6, where 0 is Monday and 6 is Sunday.
3. **Temperature** – Ambient temperature in degrees Celsius.
4. **Rainfall** – Amount of rainfall in millimeters.
5. **Holiday** – Indicates whether the day is a holiday or a regular day.

## Output

The main output of the project is:

**Predicted Traffic Volume – Number of vehicles per hour.**

The Streamlit application also categorizes the predicted traffic into:

* Free-flowing traffic
* Moderate-density traffic
* Heavy congestion

## Machine Learning Algorithm

### Random Forest Regressor

The project uses the Random Forest Regressor algorithm for predicting traffic volume.

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to produce a more reliable prediction.

In this project, the model is configured with:

* 150 decision trees
* Maximum tree depth of 10
* Random state of 42

The dataset is divided into:

* 80% training data
* 20% testing data

## Model Evaluation

The trained model is evaluated using:

### Mean Absolute Error (MAE)

Measures the average difference between the actual and predicted traffic volume.

### Root Mean Squared Error (RMSE)

Measures prediction error while giving greater importance to larger errors.

### R² Score

Shows how well the model explains the variation in traffic volume.

## Project Structure

```text
Traffic_Volume_Prediction_Sklearn/
│
├── data/
│   └── traffic_volume.csv
│
├── app.py
├── predict.py
├── train_model.py
├── traffic_volume_model.pkl
├── feature_importance.png
├── requirements.txt
├── README.md
└── HOW_TO_RUN.md
```

## Description of Files

### train_model.py

This file:

* Loads the traffic dataset.
* Selects the input features.
* Separates features and target values.
* Splits the data into training and testing sets.
* Trains the Random Forest Regressor.
* Evaluates the model.
* Saves the trained model.
* Generates a feature importance chart.

### predict.py

This is a command-line prediction program.

It asks the user to enter:

* Hour
* Day of week
* Temperature
* Rainfall
* Holiday status

It then uses the trained model to predict the traffic volume.

### app.py

This file creates the Streamlit web application.

The application provides:

* Traffic volume prediction
* Traffic congestion assessment
* Different traffic scenario presets
* Feature importance visualization
* 24-hour traffic curve
* Historical traffic data
* Operational recommendations

### traffic_volume_model.pkl

This file contains the trained Random Forest machine learning model.

### feature_importance.png

This image displays the importance of each input feature in predicting traffic volume.

### traffic_volume.csv

This is the dataset used for training and evaluating the machine learning model.

### requirements.txt

Contains the Python libraries required to run the project.

## How to Install

Open a terminal inside the project directory and run:

```bash
pip install -r requirements.txt
```

## How to Train the Model

Run:

```bash
python train_model.py
```

The program trains the Random Forest model and generates:

```text
traffic_volume_model.pkl
feature_importance.png
```

## How to Make a Prediction

Run:

```bash
python predict.py
```

The program asks for values such as:

```text
Hour (0-23):
Day of week (0=Monday, 6=Sunday):
Temperature in Celsius:
Rain in mm:
Holiday? (1=Yes, 0=No):
```

After entering the values, the system displays the predicted number of vehicles.

## How to Run the Web Application

The project includes a Streamlit application.

Run:

```bash
streamlit run app.py
```

The application provides an interactive interface where users can enter traffic and weather conditions and receive a predicted traffic volume.

## Traffic Classification

The application classifies traffic based on the predicted number of vehicles per hour.

```text
Below 400 vehicles/hr
Free-flowing traffic

400–649 vehicles/hr
Moderate-density traffic

650 vehicles/hr and above
Heavy congestion
```

## Traffic Scenario Presets

The application provides predefined scenarios such as:

* Morning rush hour
* Evening peak traffic
* Rainy midday traffic
* Midnight free-flow traffic
* Public holiday traffic

These presets make it easier to test the prediction system.

## Feature Importance

The model calculates feature importance to identify which input variables have the greatest influence on traffic volume.

The results are displayed using a horizontal bar chart generated with Matplotlib.

## 24-Hour Traffic Curve

The application can generate predicted traffic volume for every hour from 00:00 to 23:00.

This helps visualize how traffic volume changes throughout a day.

## Applications

Traffic volume prediction can be useful for:

* Traffic management
* Road planning
* Transportation planning
* Traffic signal management
* Congestion monitoring
* Urban infrastructure planning
* Intelligent Transportation Systems
* Travel planning

## Advantages

* Simple and easy to use.
* Uses machine learning for prediction.
* Supports interactive predictions.
* Provides feature importance analysis.
* Includes visualization of traffic trends.
* Can be extended with additional traffic and weather data.

## Limitations

The included dataset is synthetic and intended for educational demonstration.

Real-world traffic prediction should consider additional factors such as:

* Accidents
* Road construction
* Traffic signals
* Special events
* Road conditions
* Vehicle types
* Real-time traffic sensor data
* Local traffic patterns

## Future Enhancements

The project can be improved by:

* Using real-time traffic data.
* Adding GPS and location information.
* Including road and lane information.
* Adding weather forecast data.
* Using advanced time-series models.
* Adding live traffic APIs.
* Deploying the application online.
* Adding interactive maps and traffic visualization.

## Conclusion

Traffic Volume Prediction demonstrates how machine learning can be used to estimate traffic flow from time, weather, and holiday information.

The Random Forest Regressor provides the prediction model, while Python, Pandas, Scikit-learn, Matplotlib, Joblib, and Streamlit are used to build the complete system.

This project provides a practical introduction to machine learning-based traffic prediction and can serve as a foundation for developing more advanced intelligent transportation systems.
