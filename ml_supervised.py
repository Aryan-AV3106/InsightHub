from colorama import *
import pandas as pd
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
    if y.dtype == "object":
        y = y.astype("category").cat.codes

    return features,x,y

def clean(x):

    x = x.copy()

    for col in x.select_dtypes(include=["number"]).columns:
        x[col] = x[col].fillna(x[col].median())

    for col in x.select_dtypes(exclude=["number"]).columns:
        x[col]=x[col].fillna("Unknown")

    # encoding the columns using onehot encode
    x = pd.get_dummies(x, drop_first=True)

    return x 



def Linear_regression(df):
    result = pre_process(df)
    if result is None:
        return
    features,x,y = result
    x = clean(x)
    
    # Train Test split
    x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,  # 20 % data
    random_state=42
    )

    ## Training the model
    model = linear_model.LinearRegression()
    model.fit(x_train,y_train)


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


def Logistic_Regression(df):
    result = pre_process(df)
    if result is None:
        return
    features,x,y = result
    x = clean(x)

    # Train Test split
    x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,  # 20 % data
    random_state=42
    )

    # scalling 
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = LogisticRegression()
    model.fit(x_train_scaled,y_train)


    pred_test_y = model.predict(x_test_scaled)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))

def KNN(df):
    result = pre_process(df)
    if result is None:
        return
    features,x,y = result
    x = clean(x)

    # Train Test split
    x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,  # 20 % data
    random_state=42
    )

    # scalling 
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = KNeighborsClassifier()
    model.fit(x_train_scaled,y_train)


    pred_test_y = model.predict(x_test_scaled)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    

def decision_tree(df):
    result = pre_process(df)
    if result is None:
        return
    features,x,y = result
    x = clean(x)

    # Train Test split
    x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,  # 20 % data
    random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train,y_train)

    pred_test_y = model.predict(x_test)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    

def svm(df):
    result = pre_process(df)
    if result is None:
        return
    features,x,y = result
    x = clean(x)

    # Train Test split
    x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,  # 20 % data
    random_state=42
    )

    # scalling 
    scaler = StandardScaler()
    x_train_scaled = scaler.fit_transform(x_train)
    x_test_scaled = scaler.transform(x_test)

    model = SVC(kernel= 'rbf')
    model.fit(x_train_scaled,y_train)

    pred_test_y = model.predict(x_test_scaled)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    

def random_forest(df):
    result = pre_process(df)
    if result is None:
        return
    features,x,y = result
    x = clean(x)

    # Train Test split
    x_train,x_test,y_train,y_test = train_test_split(
    x,
    y,
    test_size=0.2,  # 20 % data
    random_state=42
    )

    model = RandomForestClassifier()
    model.fit(x_train,y_train)

    pred_test_y = model.predict(x_test)
    acc = accuracy_score(y_test,pred_test_y)
    matrix = confusion_matrix(y_test,pred_test_y)
    print(Fore.GREEN + f"Accuracy: {acc}\n confusion Matrix: {matrix}")
    print(classification_report(y_test,pred_test_y))
    
