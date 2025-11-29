![alt text](image.png)
##InsightHub

InsightHub is a command-line tool I built to load, clean, analyze, and visualize datasets.
It uses Python, Pandas, Matplotlib, and SQLite. The goal of the project is to have a simple, modular data analysis workflow that currently runs entirely in a terminal.

##Features

Data
Load CSV or Excel files.
-The dataset name and timestamp are stored in a local SQLite database so you can keep track of files you've worked with.

#Basic Analysis
-View summary statistics, find missing values, and inspect individual columns.
The goal is to quickly understand data quality and the overall structure of the dataset.

#Data Cleaning
-Sort data, fill missing values, and export cleaned versions.
This helps prepare the dataset for further analysis, reporting, or modeling.

#Visualizations
-Generate simple plots using Matplotlib:
Histogram
Bar chart
Line plot
Scatter plot
Box plot
Pie chart

#History Tracking
-All actions (summaries, cleaning steps, etc.) are saved in an SQLite history table for future refrence.

#Dataset Management
-View existing datasets, check their timestamps, and delete old entries if needed.

##Project Structure

InsightHub/
│
├── main_cli.py
├── analytics.py
├── data_handler.py
├── database.py
├── visulalize.py
└── README.md

##Installation:

Clone the repository:
git clone https://github.com/yourusername/InsightHub.git
cd InsightHub

Install the required libraries:
pip install pandas matplotlib openpyxl colorama

#How to Run

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
9. Exit

Choose an option and follow the prompts.

#Design & Architecture
-InsightHub is written using a class-based (OOP) structure.
The main class maintains the state of the current dataset and routes menu options to the appropriate modules.

The code is split across separate files:

data_handler.py – reading CSV/Excel files
analytics.py – summary, missing values, column analysis, sort file, fill missing, export the updated file.
visulalize.py – plotting functions
database.py – SQLite interaction
main.py – Main menu and insighthub class

#Upcoming:

- Streamlit UI version of InsightHub
- Basic machine learning support, including:
  Linear Regression
  Logistic Regression
  Decision Trees
  K-Means clustering

Notes
-Visualizations open in a separate Matplotlib window.
-The SQLite database file stores dataset names, insights, and action history.
-The code is written in a modular way so new features can be added easily (e.g., more visualizations, ML models, or a GUI/Streamlit version later).

Author:
Aryan Hemangbhai Vakharia
