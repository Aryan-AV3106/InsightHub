import matplotlib.pyplot as plt
import os
from datetime import datetime as dt
from database import save_history
import pandas as pd 
from colorama import Fore, Back, Style, init
init(autoreset=True)


def ask_to_save_plot(default_name):
    choice = input(Fore.YELLOW + f"Would you like to save the plot (y/n): ").strip().lower()

    if choice != "y":
        print(Fore.RED +"Plot is not saves.\n")
        return None
    
    if not os.path.exists("exports/plots"):
        os.makedirs("exports/plots")
    
    name = input(Fore.YELLOW + f"Name of the plot: ")

    if name == "":
        print(Fore.RED + f"No name entered\n")
        print(Fore.RED + f"Using default Name\n")
        name = default_name
    
    time = dt.now().strftime("%y%m%d_%H%M%S")
    path = f"exports/plots/{name}_{time}.png"
    plt.savefig(path)
    return path

def plot_histogram(df):
    plt.clf()
    col = input("Enter the column name: ")

    if col not in df.columns:
        print(Fore.RED + "Column not found in the database.")
        return
    
    if df[col].dtype != 'object':

        plt.hist(df[col], bins = 3)
        plt.show()
        save_history(f"Histogram viewed for the column {col}.")
        ask_to_save_plot("Histogram")
    else :
        print(Fore.RED + f"Column {col} is not numeric.")
        
def plot_line(df):
    plt.clf()
    col = input("Enter the column name: ")

    if col not in df.columns:
        print(Fore.RED + "Column not found in the database.")
        return
    
    if df[col].dtype != 'object':

        plt.plot(df[col], color= "blue",marker = "o", linewidth = 2,  )
        plt.show()
        save_history(f"Line Plot viewed for the column {col}.")
        ask_to_save_plot("line_plot")

    else :
        print(Fore.RED + f"Column {col} is not numeric.")
def plot_box(df):
    plt.clf()
    col = input("Enter the column name: ")

    if col not in df.columns:
        print(Fore.RED + "Column not found in the database.")
        return
    
    if df[col].dtype != 'object':
        plt.boxplot(df[col].dropna())
        plt.show()
        save_history(f"Box Plot viewed for the column {col}.")
        ask_to_save_plot("box_plot")
    else :
        print(Fore.RED + f"Column {col} is not numeric.")
# for two numerical columns 
def plot_Scatter(df):
    plt.clf()
    col1 = input("Enter the First column name(x - axis): ")
    col2 = input("Enter the Second column name(y - axis): ")

    if col1 not in df.columns or col2 not in df.columns:
        print(Fore.RED + "One of the Column not found in the databases.")
        return
    
    if df[col1].dtype != 'object' and df[col2].dtype != 'object':
        plt.scatter(df[col1],df[col2],color = "blue")
        plt.show()
        save_history(f"Scatter Plot viewed for the column{col1} and the column{col2}.")
        ask_to_save_plot("Scatter_plot")
    else :
        print(Fore.RED + f"1 of the column entered is not numeric.")

# for categorical columns
def plot_bar(df):
    plt.clf()
    col = input("Enter the column name: ")

    if col not in df.columns:
        print(Fore.RED + "Column not found in the database.")
        return
    
    if df[col].dtype == 'object':
        count = df[col].value_counts()
        plt.bar(count.index, count.values)
        plt.show()
        save_history(f"Bar Plot viewed for the column {col}.")
        ask_to_save_plot("Bar_plot")
    else :
        print(Fore.RED + f"Column {col} is not Categorical.")

def plot_pie(df):
    plt.clf()
    col = input("Enter the column name: ")

    if col not in df.columns:
        print(Fore.RED + "Column not found in the database.")
        return
    
    if df[col].dtype == 'object':
        count = df[col].value_counts()
        plt.pie(count.values,labels = count.index,autopct= "%1.2f")
        plt.show()
        save_history(f"Pie Plot viewed for the column {col}.")
        ask_to_save_plot("pie_plot")
    else :
        print(Fore.RED + f"Column {col} is not Categorical.")
