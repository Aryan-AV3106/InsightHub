from colorama import *
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,r2_score,accuracy_score,confusion_matrix,classification_report

def pre_process(df):
    feature = input(Fore.BLUE + "Enter feature columns separated by commas : ")
    feature = feature.split(",")
    features = []
    for i in feature: 
        if i.strip() not in df.columns:
            print(Fore.RED +"Column not found.\n please Try again.\n")
            return None
        features.append(i.strip())

    x = df[features] # x axis 2D array

    target = input(Fore.BLUE + "Please enter a single Target coulmn name.").strip()
    if target not in df.columns:
        print(Fore.RED +"Column not found.\n please Try again.\n")
        return  None
    y = df[target] # y axis 1D array

    ## spliting the data into training and Test datasets(4:1)

    x_train,x_test,y_train,y_test = train_test_split(
        x,
        y,  
        train_size= 0.8,
        random_state= 42
    )
    return features,x_train,x_test,y_train,y_test

def predict(model,features,scaler = None):
    while True:
        c = input(Fore.BLUE + "Would you like to predict more values (y/n)?")
        if c.lower() == "y":
            predict = []
            for feature in features:
                while True:
                    f = input(Fore.BLUE + f"please enter the feature value for {feature}")
                    try:
                        f = float(f)
                        predict.append(f)
                        break
                    except:
                        print(Fore.RED +"Input is not a numeric value.\nPlease try again.\n")

            new_df = pd.DataFrame([predict],columns=features)
            # for algorithms with scaled data
            if scaler is not None:
                new_df = scaler.transform(new_df)
            pred = model.predict(new_df)
            print(Fore.GREEN +f"predicted target is : {pred[0]}")            
            
        elif c.lower() == "n":
            print("Thank You\n")
            break

        else:
            print(Fore.RED +"\nInvalid Choice!!!\nEnter a valid choice.\n")


def Linear_regression(df):
    result = pre_process(df)
    if result is None:
        return
    features,x_train,x_test,y_train,y_test = result

    ## Training the model
    model = linear_model.LinearRegression()
    try:
        model.fit(x_train,y_train)
    except:
        print(Fore.RED +"Column is not numeric.\n please use a numeric column.\n")
        return

    pred_y = model.predict(x_train) # predicted y for training data

    # predicted y for test
    pred_test_y = model.predict(x_test)

    # Train MAE and R^2
    train_mae = mean_absolute_error(y_train,pred_y)
    train_r2 = r2_score(y_train,pred_y) 
    print(Fore.GREEN + f"Train Mae: {train_mae}\nTrain R^2: {train_r2}")

    # Test MAE and R^2
    test_mae = mean_absolute_error(y_test,pred_test_y)
    test_r2 = r2_score(y_test,pred_test_y) 
    print(Fore.GREEN + f"Test Mae: {test_mae}\nTest R^2: {test_r2}")

    # Baseline MAE and R^2
    mean = y_train.mean()
    y_baseline_pred = [mean] * len(y_test)
    baseline_mae = mean_absolute_error(y_test,y_baseline_pred)
    baseline_r2 = r2_score(y_test,y_baseline_pred)
    print(Fore.GREEN + f"Baseline Mae: {baseline_mae}\nBaseline R^2: {baseline_r2}")

    # new predictions
    predict(model,features)

def Logistic_Regression(df):
    result = pre_process(df)
    if result is None:
        return
    features,x_train,x_test,y_train,y_test = result

    # scalling 
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = LogisticRegression()
    try:
        model.fit(x_train_scaled,y_train)
    except:
        print(Fore.RED +"Column is not numeric.\n please use a numeric column.\n")
        return

    pred_test_y = model.predict(x_test_scaled)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))

    # new predictions
    predict(model,features,scaler)

def KNN(df):
    result = pre_process(df)
    if result is None:
        return
    features,x_train,x_test,y_train,y_test = result

    # scalling 
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = KNeighborsClassifier()
    try:
        model.fit(x_train_scaled,y_train)
    except:
        print(Fore.RED +"Column is not numeric.\n please use a numeric column.\n")
        return

    pred_test_y = model.predict(x_test_scaled)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    
    # new predictions
    predict(model,features, scaler)

def decision_tree(df):
    result = pre_process(df)
    if result is None:
        return
    features,x_train,x_test,y_train,y_test = result

    model = DecisionTreeClassifier(random_state=42)
    try:
        model.fit(x_train,y_train)
    except:
        print(Fore.RED +"Column is not numeric.\n please use a numeric column.\n")
        return

    pred_test_y = model.predict(x_test)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    
    # new predictions
    predict(model,features)

def svm(df):
    result = pre_process(df)
    if result is None:
        return
    features,x_train,x_test,y_train,y_test = result

    # scalling 
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = SVC(kernel= 'rbf')
    try:
        model.fit(x_train_scaled,y_train)
    except:
        print(Fore.RED +"Column is not numeric.\n please use a numeric column.\n")
        return

    pred_test_y = model.predict(x_test_scaled)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    
    # new predictions
    predict(model,features, scaler)

def random_forest(df):
    result = pre_process(df)
    if result is None:
        return
    features,x_train,x_test,y_train,y_test = result

    model = RandomForestClassifier()
    try:
        model.fit(x_train,y_train)
    except:
        print(Fore.RED +"Column is not numeric.\n please use a numeric column.\n")
        return

    pred_test_y = model.predict(x_test)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    
    # new predictions
    predict(model,features)

