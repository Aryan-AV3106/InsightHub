import pandas as pd
from database import *
import os 
from datetime import datetime as dt 
from colorama import Fore, Back, Style, init
init(autoreset=True)
# Update file methods 
# sorting file
def sort_file(df):
    col = input(Fore.BLUE + "Enter the coulmn name you would like to sort according to: ").strip()
    if col not in df.columns:
        print(Fore.RED +"Column not found !!!\n")
        return df 
    
    df = df.sort_values(col, ascending= False)
    print(Fore.GREEN +"Sorted successfully.\n")
    return df    

# filled missing 
def fill_missing(df):
    col = input(Fore.BLUE + "Enter the coulmn name you want to fill missing values for: ").strip()
    if col not in df.columns:
        print(Fore.RED +"Column not found !!!\n")
        return df
    
    if df[col].dtype != 'object':
        df[col] = df[col].fillna(df[col].median())
        print(f"Missing values in '{col}' filled using median.\n")

    else:
        df[col] = df[col].fillna(df[col].mode()[0])
        print(f"Missing values in '{col}' filled using mode.\n")
        
    return df

# Exporting file
def export_file(df):
    # make folder name exports
    if not os.path.exists("exports"):
        os.makedirs("exports")
    
    print(Fore.CYAN+ Style.BRIGHT +"\nExport format:")
    print(Fore.YELLOW +"1. Export as CSV")
    print(Fore.YELLOW +"2. Export as Excel")
    print(Fore.YELLOW +"3. Cancel Export")
    
    try: 
        ch = int(input(Fore.BLUE + "Enter Choice: "))
    except:
        print(Fore.RED +"Invalid choice\nPlease try again.\n")
        return
    if ch == 1:
        time = dt.now().strftime("%Y%m%d_%H%M%S")
        f_Name = input(Fore.BLUE + "Enter the name of output file (without extension)").strip()
        #Empty file name
        if f_Name == "":
            print(Fore.RED +"Empty file name")
            print(Fore.RED +"Default name 'export' used instead")
            f_Name = "export"

        f_Name = f"exports/{f_Name}_{time}.csv"
        df.to_csv(f_Name,index = False)
        print(Fore.GREEN +f"\nFile exported as CSV: {f_Name}\n")

    elif ch == 2:
        time = dt.now().strftime("%Y%m%d_%H%M%S")
        f_Name = input(Fore.BLUE + "Enter the name of output file (without extension)").strip()
        #Empty file name
        if f_Name == "":
            print(Fore.RED +"Empty file name")
            print(Fore.RED +"Default name 'export' used instead")
            f_Name = "export"

        f_Name = f"exports/{f_Name}_{time}.xlsx"
        try:
            df.to_excel(f_Name,index = False)
        except:
            print(Fore.RED +"No openpyxl Found.\nopen terminal and download 'pip install openpyxl'")
        print(Fore.GREEN +f"\nFile exported as Excel: {f_Name}\n")
        
    elif ch == 3: 
        print(Fore.RED +"Export Cancelled.\n")
        return
    else:
        print(Fore.RED +"Invalid choice\nPlease try again.\n")
        return
        
# view insights methods 
# show summary 
def show_basic_summary(df,current_dataset_id):
    print(Fore.CYAN +Style.BRIGHT +"\nBasic file details\n")
    print(Style.RESET_ALL, end="")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    print("Columns: ",",".join(df.columns)) # prints the column names
    
    num_cols = df.select_dtypes(include=["number"]).columns
    cat_cols = df.select_dtypes(include=["object","category"]).columns
    
    print("Numeric columns: ",",".join(num_cols))
    print("Categorical columns: ",",".join(cat_cols))

    print(Fore.CYAN +Style.BRIGHT +"\nStatistics")
    if len(num_cols) == 0:
        print(Fore.RED +"No numeric columns in data\n")
    else:
        print(df.describe())
    
    # storing insights
    text = f"Summary viewed: {df.shape[0]} rows, {df.shape[1]} columns.\nNumeric columns: {len(num_cols)} | Categorical columns: {len(cat_cols)}"
    save_insight(current_dataset_id,text)

# show missing data
def show_missing_data(df,current_dataset_id):
    null_count = df.isnull().sum()
    percent = null_count/len(df)*100
    if null_count.sum() == 0:
        print(Fore.RED +"No missing values detected\n")

        # storing insights
        text = f"Missing Values viewed,\nNO missing values detected"
        save_insight(current_dataset_id,text)

        return

    else:
        missing_columns = (null_count > 0).sum()
        print(Style.RESET_ALL, end="")
        print(f"Found missing values in {missing_columns} columns.\n")
        new_df = pd.DataFrame({
            "Missing values" : null_count,
            "Percentage" : percent.round(2),
        })
        print(new_df)
        print()
        # storing insights
        text = f"Missing Values viewed,\nFound missing values in {missing_columns} columns."
        save_insight(current_dataset_id,text)

# view column analysis
def show_column_analysis(df,current_dataset_id):
    col = input(Fore.BLUE + "Please enter the Column name: ").strip()

    if col not in df.columns:
        print(Fore.RED +"Column not found.\n please Try again.\n")
        return
    print(Fore.CYAN +Style.BRIGHT +"\nColumn Analysis\n")

    # Numeric Column
    if df[col].dtype != "object":
        print(Fore.CYAN +Style.BRIGHT +f"Numeric Column Analysis for {col}")
        print(Style.RESET_ALL, end="")
        print(f"Maximum : {df[col].max()}") 
        print(f"Minimum : {df[col].min()}") 
        print(f"Mean    : {df[col].mean()}") 
        print(f"Missing : {df[col].isnull().sum()}")
        print(f"Unique  : {df[col].nunique()}")
        print()

        # storing insights
        text = f"Column Analysis viewed, {col}: Numeric Column\nMax : {df[col].max()}\nMin : {df[col].min()}\nMean : {df[col].mean()}"
        save_insight(current_dataset_id,text)

    # Categorical Column
    elif df[col].dtype == "object":
        missing_count = df[col].isnull().sum()
        unique_categories = df[col].nunique()
        print(Fore.CYAN +Style.BRIGHT +f"Categorical Column Analysis for {col}")
        print(Style.RESET_ALL, end="")
        print(f"Unique Categories : {unique_categories}") 
        print(f"Missing : {missing_count}") 
        print(f"Most frequent Category : {df[col].mode()[0]}") 
        print(df[col].value_counts().head())
        print()

        # storing insights
        text = f"Column Analysis viewed, {col}: Categorical Column\nUnique Categories : {unique_categories}\nMost frequent Category : {df[col].mode()[0]}"
        save_insight(current_dataset_id,text)