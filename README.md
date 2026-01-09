![alt text](image.png)
## InsightHub

InsightHub is a command-line tool I built to load, clean, analyze, and visualize datasets.
I mainly built it to avoid switching between multiple scripts and notebooks while working with real datasets.

## Features

Data
Load CSV or Excel files.
-The dataset name and timestamp are stored in a local SQLite database so you can keep track of files you've worked with.

## Basic Analysis
-View summary statistics, find missing values, and inspect individual columns.
The goal is to quickly understand data quality and the overall structure of the dataset.

## Data Cleaning
-Sort data, fill missing values, and export cleaned versions.
This helps prepare the dataset for further analysis, reporting, or modeling.

## Visualizations
-Generate simple plots using Matplotlib:
Histogram
Bar chart
Line plot
Scatter plot
Box plot
Pie chart

## Supervisde Machine Learning
Train and evaluate models directly from the CLI:
Linear Regression (Regression)
Logistic Regression
K-Nearest Neighbors
Decision Tree
Support Vector Machine
Random Forest


Each model includes:
Train/test split
Appropriate valuation metrics
Interactive prediction on new inputs

## History Tracking
-All actions (summaries, cleaning steps, etc.) are saved in an SQLite history table for future reference.

## Dataset Management
-View existing datasets, check their timestamps, and delete old entries if needed.

## Project Structure

InsightHub/

│
├── main_cli.py
├── analytics.py
├── data_handler.py
├── database.py
├── visualize.py
└── README.md

## Installation:

Clone the repository:
git clone (https://github.com/Aryan-AV3106/InsightHub)
cd InsightHub

Install the required libraries:
pip install pandas matplotlib openpyxl scikit-learn colorama

## How to Run

Inside the project folder:
python main.py

This will open the menu:

1. Add / Load Data
2. View Insights
3. Update Data
4. View Saved Insights
5. Show Saved History
6. View Existing Datasets
7. Delete Existing Datasets
8. Visualize Columns
9. ML Supervised
10. Exit

Choose an option and follow the prompts.

## Design & Architecture
-InsightHub is written using a class-based (OOP) structure.
The main class maintains the state of the current dataset and routes menu options to the appropriate modules.

The code is split across separate files:

data_handler.py – reading CSV/Excel files
analytics.py – summary, missing values, column analysis, sort file, fill missing, export the updated file.
visulalize.py – plotting functions
ml_supervised.py - Supervised ML algorithms
database.py – SQLite interaction
main.py – Main menu and insighthub class

## Case Studies

# Case Study 1: Kaggle EV Energy Efficiency Prediction (Regression)

I used InsightHub to test a real-world electric vehicle dataset with 1,197 rows and a mix of numerical and categorical features.

# Goal:
Predict a vehicle’s energy efficiency (km/kWh) using supervised learning.

# Features I used:
Model year
Vehicle class (categorical)
Motor power (kW)
Recharge time (hours)

# Model used:
Linear Regression

# Results:
Test MAE ≈ 0.46
Test R² ≈ 0.53
Baseline MAE ≈ 0.69
Baseline R² ≈ −0.01

# Takeaway 
The regression model clearly performed better than the baseline and showed similar performance on training and test data, which suggests it generalized well. This experiment showed that InsightHub can handle real datasets with mixed feature types and produce meaningful regression results without manual preprocessing outside the tool.

# Case Study 2: Kaggle Diabetes Prediction (Classification)

I also tested InsightHub on a larger healthcare dataset with 10,000 records and 20 features to evaluate its classification capabilities.

# Goal:
Predict whether a person has diabetes (binary classification).

# Features I used:
Age, gender, BMI
Glucose, blood pressure, cholesterol
Heart rate, physical activity
Smoking status, family history

# Models tested:
Logistic Regression
Random Forest
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)

# Results:
Accuracy across models was around 49–50%
Confusion matrices were fairly balanced
Precision, recall, and F1 scores were similar across models

# Takeaway :
Since all models performed similarly, this suggests that the dataset has noise due to the selected features. This proves improving features and data quality often matters more than switching between algorithms. 
-> It also showed that InsightHub can be used to fairly compare multiple models on the same dataset.

## Upcoming:

- Streamlit UI version of InsightHub
- Model comparison dashboard
- Unsupervised learning (K-Means)

Notes
-Visualizations open in a separate Matplotlib window.
-The SQLite database file stores dataset names, insights, and action history.
-The code is written in a modular way so new features can be added easily (e.g., more visualizations, ML models, or a GUI/Streamlit version later).

Author:
Aryan Hemangbhai Vakharia
