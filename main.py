from database import setup_database
from data_handler import load_data,get_file_path
from visualize import *
from analytics import *
from database import *
from ml_supervised import *
from colorama import Fore, Back, Style, init
init(autoreset=True)

class InsigtHub():

    def __init__(self):
        self.df = None
        self.dataset_id = None 
        self.f_name = None
        setup_database()

    def run(self):
        while(True):
            print(Fore.CYAN +Style.BRIGHT + "\n-----InsightHub-----")
            print(Fore.YELLOW + "1. Add / Load Data.")
            print(Fore.YELLOW + "2. View Insights.")
            print(Fore.YELLOW + "3. Update Data.")
            print(Fore.YELLOW + "4. View Saved Insights.")
            print(Fore.YELLOW + "5. Show Saved History.")
            print(Fore.YELLOW + "6. View Existing Datasets.")
            print(Fore.YELLOW + "7. Delete Existing Datasets.")
            print(Fore.YELLOW + "8. Visualize Columns.")
            print(Fore.YELLOW + "9. ML supervised.")
            print(Fore.YELLOW + "10. Exit")
            try:
                choice = int(input(Fore.BLUE + "Enter choice: "))
            except:
                print(Fore.RED +"\nInvalid Choice!!!\nEnter a valid choice.\n")
                continue
            # Add/ Load data
            if(choice == 1):
                self.load_file()
            # View insights 
            elif(choice == 2):
                self.view_insights()
            # Update Data
            elif(choice == 3):
                self.update_data()
            # view already stored insight 
            elif(choice == 4):
                self.view_saved_insights()
            # get history from sql
            elif(choice == 5):
                self.show_saved_history()
            # get Existing datasets
            elif ( choice == 6 ): 
                self.view_existing_datasets()
            # delete Existing datasets
            elif (choice == 7):
                self.delete_existing_dataset()
            # visualize data
            elif(choice == 8):
                self.visualize()
            # train supervised ml models
            elif(choice == 9):
                self.ml_supervised()
            # Exit        
            elif(choice == 10):
                print(Fore.CYAN + Style.BRIGHT +"Thank You for using InsightHub.\n")
                break
            # Invalid choice
            else:
                print(Fore.RED +"\nInvalid Choice!!!\nEnter a valid choice.\n")
                continue

    def load_file(self):
        print()
        print(Fore.YELLOW +"1. Load CSV file")
        print(Fore.YELLOW +"2. Load EXCEL file")
        try:
            c = int(input(Fore.BLUE + "Enter choice:"))
        except:
            print(Fore.RED +"Invalid choice!!1\nPlease enter a valid choice.\n")
            return 
        # Csv file
        if c == 1:
            self.df,self.f_name = load_data("csv")
            save_dataset(self.f_name)
            self.dataset_id = get_dataset_id(self.f_name)
        # Excel file
        elif c == 2:
            self.df,self.f_name = load_data("excel")
            save_dataset(self.f_name)
            self.dataset_id = get_dataset_id(self.f_name)
        else:
            print(Fore.RED +"\nInvalid choice, please enter a valid choice\n")
            return

    def view_insights(self):
        if self.df is None:
            print(Fore.RED +"No dataset loaded yet\nPlease load a dataset first.\n")
            return
        else:
            while(True):
                print()
                print(Fore.CYAN +Style.BRIGHT + "What would You like to do:")
                print(Fore.YELLOW +"1. Summary")
                print(Fore.YELLOW +"2. Missing Values")
                print(Fore.YELLOW +"3. Column Analysis")
                print(Fore.YELLOW +"4. Back")
                try:
                    ch = int(input(Fore.BLUE + "Enter choice: "))
                except:
                    print(Fore.RED +"Invalid choice!!!\nPlease enter a valid choice.\n")
                    continue
                # view summary
                if ch == 1:
                    show_basic_summary(self.df,self.dataset_id)
                    history = "Read Basic Summary."
                    save_history(history)
                # view missing data
                elif ch == 2:
                    show_missing_data(self.df,self.dataset_id)
                    history = "Checked for Missing values"
                    save_history(history)
                # view column Analysis
                elif ch == 3:
                    show_column_analysis(self.df,self.dataset_id)
                    history = "Viewed Column Analysis"
                    save_history(history)
                # return
                elif ch == 4:
                    return
                else:
                    print(Fore.RED +"Invalid choice!!!\nPlease enter a valid choice.\n")
                    continue
                
    def update_data(self):
        if self.df is None:
            print(Fore.RED +"No data set loaded yet\nPlease load a dataset first.\n")
            return 
        else:
            while(True):
                print()
                print(Fore.CYAN +Style.BRIGHT +"How would you like to update your file:")
                print(Fore.YELLOW +"1. Sort")
                print(Fore.YELLOW +"2. Fill missing value")
                print(Fore.YELLOW +"3. Export File(CSV/EXCEL).")
                print(Fore.YELLOW +"4. Return to main menu")
                print()
                try:
                    ch = int(input(Fore.BLUE + "Enter choice: "))
                except:
                    print(Fore.RED +"Invalid choice!!!\nPlease enter a valid choice.\n")
                    continue
                # sorting
                if ch == 1:
                    self.df = sort_file(self.df)
                    history = "File Sorted"
                    save_history(history)
                # Fill missing 
                elif ch == 2:
                    self.df = fill_missing(self.df)
                    history = "Filled Missing values"
                    save_history(history)
                # Export
                elif ch == 3:
                    export_file(self.df)
                    history = "Exported cleaned file"
                    save_history(history)
                # return
                elif ch == 4:
                    return
                else:
                    print(Fore.RED +"Invalid choice!!!\nPlease enter a valid choice.\n")
                    continue

    def view_saved_insights(self):
        if self.df is None:
            print(Fore.RED +"No data set loaded yet\nPlease load a dataset first.\n")
            return
        insightlist = get_insights(self.dataset_id)
        if not insightlist:
            print(Fore.RED +f"No previous insights found for the dataset '{self.f_name}'\n")
            return 
        else:
            print(Style.RESET_ALL, end="")
            for insight, timestamp in insightlist:
                print(f"[{timestamp}] - {insight}")
            return

    def show_saved_history(self):
        history_list = get_history()
        if not history_list: 
            print(Fore.RED +"No history found.\n")
        else:
            print(Style.RESET_ALL, end="")
            for action, timestamp in history_list:
                print(f"[{timestamp}] - {action}")
            print()

    def view_existing_datasets(self):
        print(Style.RESET_ALL, end="")
        dataset_list = get_datasets()
        if not dataset_list:
            print (Fore.RED +"No datasets stored yet.\n")
        else:
            print(Style.RESET_ALL, end="")
            for dataset_id, name, timestamp in dataset_list:
                print(f"ID: {dataset_id} | Name: {name} | Loaded at: {timestamp}")
            print()

    def delete_existing_dataset(self):
        print(Style.RESET_ALL, end="")  

        # reprinting the existing databases
        dataset_list = get_datasets()
        if not dataset_list:
            print (Fore.RED +"No datasets stored yet.\n")
        else:
            print(Style.RESET_ALL, end="")
            for dataset_id, name, timestamp in dataset_list:
                print(f"ID: {dataset_id} | Name: {name} | Loaded at: {timestamp}")
            print()
        # Delete 
        try:
            dataset_id = int(input("Please enter the dataset id of the dataset you would like to delete: "))
        except:
            print(Fore.RED +f"Dataset ID is an Integer.\n")
            return
        delete_datasets(dataset_id)


    def visualize(self):
        if self.df is None:
            print(Fore.RED +"No data set loaded yet\nPlease load a dataset first.\n")
            return 
        while(True):
            print(Fore.CYAN +Style.BRIGHT + "\nVisualize")
            print(Fore.YELLOW + "1. Histogram.")
            print(Fore.YELLOW + "2. Bar Chart.")
            print(Fore.YELLOW + "3. Line Plot.")
            print(Fore.YELLOW + "4. Scatter Plot.")
            print(Fore.YELLOW + "5. Box Plot.")
            print(Fore.YELLOW + "6. Pie Plot")
            print(Fore.YELLOW + "7. Back")
            try:
                choice = int(input(Fore.BLUE + "Enter choice: "))
            except:
                print(Fore.RED +"\nInvalid Choice!!!\nEnter a valid choice.\n")
                continue
            if(choice == 1):
                plot_histogram(self.df)
            elif(choice == 2):
                plot_bar(self.df)
            elif(choice == 3):
                plot_line(self.df)
            elif(choice == 4):
                plot_Scatter(self.df)
            elif(choice == 5):
                plot_box(self.df)
            elif(choice == 6):
                plot_pie(self.df)
            elif (choice == 7):
                return
            else:
                print(Fore.RED +"\nInvalid Choice!!!\nEnter a valid choice.\n")
                continue
    
    def ml_supervised(self):
        if self.df is None:
            print(Fore.RED +"No data set loaded yet\nPlease load a dataset first.\n")
            return
        
        while True:
            print(Fore.CYAN +Style.BRIGHT + "\n     |ML - Models|      ")
            print(Fore.YELLOW + "1. Linear Regression.")
            print(Fore.YELLOW + "2. Logistic Regression.")
            print(Fore.YELLOW + "3. K Nearest Neighbors.")
            print(Fore.YELLOW + "4. Decision Tree.")
            print(Fore.YELLOW + "5. Suport Vector Machine.")
            print(Fore.YELLOW + "6. Random Forest.")
            print(Fore.YELLOW + "7. Back.")

            try: 
                print()
                choice = int(input(Fore.BLUE + "Please enter your Choice : "))
            except:
                print(Fore.RED +"\nInvalid Choice!!!\nEnter a valid choice.\n")
                continue

            if choice == 1:
                Linear_regression(self.df)
                save_history("Ran Linear Regression.")
            elif choice == 2:
                Logistic_Regression(self.df)
                save_history("Ran Logistic Regression.")
            elif choice == 3:
                KNN(self.df)
                save_history("Ran K Nearest Neighbors.")
            elif choice == 4:
                decision_tree(self.df)
                save_history("Ran Decision Tree.")
            elif choice == 5:
                svm(self.df)
                save_history("Ran Suport Vector Machine.")
            elif choice == 6:
                random_forest(self.df)
                save_history("Ran Random Forest.")
            elif choice == 7:
                return
            else:
                print(Fore.RED +"\nInvalid Choice!!!\nEnter a valid choice.\n")
                continue

if __name__ == "__main__":
    app = InsigtHub()
    app.run()
