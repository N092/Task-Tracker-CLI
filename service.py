from asyncio import tasks
from model import Task
from tabulate import tabulate
from datetime import datetime
import json
from model import Task
from dataclasses import asdict

DB_PATH = "task_database.json"
# This File Handles the loading and writing of the json file
def load_database():
    try:
        with open(DB_PATH, "r") as f:
            database = json.load(f)
            return [Task(**t) for t in database]
    except FileNotFoundError:
            return []

def save_database(database):
    with open(DB_PATH,"w") as f:
        database = list(map(asdict, database))
        json.dump(database, f, indent=4)
    return True

class TaskService:
    def displayAllTask():
        print(tabulate(load_database(), headers="keys", tablefmt="rounded_outline"))

    def addTask(task_description):
        try:
            database =load_database()
            task = Task(len(database)+1,task_description,"todo",datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            database.append(task)
            save_database(database)
            return True
        except Exception as e:
            print(f"Failed to add the task error message {e}")

    def removeTask(id):
        try:
            database = [task for task in load_database() if task.id != id]
            save_database(database)
            return True
        except Exception as e:
            print(f"Failed to remove the task error message {e}")












