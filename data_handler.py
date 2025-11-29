import pandas as pd
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)
def load_data(type):
    # Gets file Name
    path = get_file_path(type)
    if path is None:
        return None,None
    name = os.path.basename(path)
    # Reads file using pandase
    df = read_file(path,type)
    if df is None:
        return None,None

    # Loading details if data loaded
    if df is not None:
        print(Fore.CYAN +Style.BRIGHT +"\nBasic file details\n")
        print(f"Total Rows: {df.shape[0]} | Total Columns: {df.shape[1]}")
        print("Columns: ",", ".join(df.columns)) # prints the column names
        print(Fore.CYAN +Style.BRIGHT +"\nPeek at the start of file\n")
        print(df.head())
        print("\nData loaded into memory. You can now select 'View Insights' from the main menu\n")
    return df,name

# Takes the input file path from the user
def get_file_path(type):
    path = input(Fore.BLUE + "Enter the full file path: ").strip()
    if not os.path.exists(path):
        print(Fore.RED +"File does not exist\n")
        return
    return path

# Reads file 
def read_file(path,type):
    # Csv file read
    if type == "csv":
        try:
            df = pd.read_csv(path)
            print(Fore.GREEN +"File loaded Successfully\n")
        except:                         # An error with file
            df = None
            print(Fore.RED +"Invalid file path\n")
        return df
    # Excel file read
    elif type == "excel":
        try:
            df = pd.read_excel(path)
            print(Fore.GREEN +"File loaded Succesfully\n")
        except:                         # An error with file
            df = None
            print(Fore.RED +"Invalid file path\n")
        return df