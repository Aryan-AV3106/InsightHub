import sqlite3
from datetime import datetime as dt
from colorama import Fore, Back, Style, init
init(autoreset=True)

def setup_database():
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()

    # Table that will store the datasets.
    curr.execute(""" CREATE TABLE IF NOT EXISTS Datasets (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 timestamp TEXT)""")
    
    # Table that will store insights.
    curr.execute(""" CREATE TABLE IF NOT EXISTS Insights (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 dataset_id INTEGER,
                 insight TEXT,
                 timestamp TEXT)""")
    
    # Table that will store history.
    curr.execute(""" CREATE TABLE IF NOT EXISTS History (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 action TEXT,
                 timestamp TEXT)""")
    
    conn.commit()
    curr.close()
    conn.close()

def save_history(action):
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    curr.execute("""INSERT INTO History(action,timestamp)
                 VALUES (?,?);""",(action,time))
    
    conn.commit()
    curr.close()
    conn.close()

def save_insight(dataset_id,insight):
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    curr.execute("""INSERT INTO Insights(dataset_id,insight,timestamp)
                 VALUES (?,?,?);
                 """,(dataset_id,insight,time))

    conn.commit()
    curr.close()
    conn.close()

def save_dataset(name):
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()
    time = dt.now().strftime("%Y-%m-%d %H:%M:%S")

    # no duplicates 
    exists = curr.execute("""SELECT id
                          FROM Datasets
                          Where name = ?
                          ORDER BY id DESC
                          LIMIT 1;""",(name,)).fetchone()
    if exists:
        curr.execute("""UPDATE Datasets
                     SET timestamp = ?
                     WHERE id = ?;""",(time,exists[0]))

    else:
        curr.execute("""INSERT INTO Datasets(name,timestamp)
                     VALUES(?,?)""",
                     (name,time))

    conn.commit()
    curr.close()
    conn.close()

def get_history():
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()
    
    data = curr.execute("""SELECT action, timestamp
                 FROM History
                 ORDER BY id DESC
                 LIMIT 20;""").fetchall()
    curr.close()
    conn.close()
    return data

def get_insights(dataset_id):
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()

    data = curr.execute("""SELECT insight, timestamp
                 FROM Insights
                 WHERE dataset_id = (?)
                 ORDER BY id DESC
                 LIMIT 20;""",(dataset_id,)).fetchall()
    curr.close()
    conn.close()
    return data

def get_dataset_id(name):
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()
    
    data = curr.execute("""SELECT id
                 FROM Datasets
                 WHERE name = (?)
                 ORDER BY id DESC
                 Limit 1;""",(name,)).fetchone()
    
    curr.close()
    conn.close()

    if data is None:
        print(f"Could not find dataset with name {name}")
        return None
    
    return data[0]

def get_datasets():
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()

    data = curr.execute("""SELECT id, name, timestamp
                     FROM Datasets
                     ORDER BY id DESC""").fetchall()

    curr.close()
    conn.close()
    return data

def delete_datasets(dataset_id):
    conn = sqlite3.connect("insighthub.db")
    curr = conn.cursor()
    curr.execute(""" DELETE 
                FROM Datasets
                WHERE id = (?);""",(dataset_id,))

    if(curr.rowcount == 0):
        print(Fore.RED + f"No dataset found with ID: [{dataset_id}]\n")
        curr.close()
        conn.close()
        return
    
    print(Fore.GREEN + f"Dataset({dataset_id}) deleted from datasets successfully.\n")

    curr.execute("""DELETE 
                 FROM Insights
                 WHERE dataset_id = (?);""",(dataset_id))

    print(Fore.GREEN + f"All the stored insights reltaed to the Dataset : [{dataset_id}] is deleted successfully.\n")
    conn.commit()
    curr.close()
    conn.close()