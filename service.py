from asyncio import tasks
from model import Task
from tabulate import tabulate
from datetime import datetime
import json
from model import Task
from dataclasses import asdict

DB_PATH = "task_database.json"

# This File Handles the loading and writing of the json file

"""
    This function load the json file and return a list containing identity_id (works like auto increment in sql) and a list which contains object of task
    
    on exception it returns a list containing 0 and empty list
"""
def load_database():
    try:
        with open(DB_PATH, "r") as f:
            database = json.load(f)
            return [database[0],[Task(**t) for t in database[1]]]
    except FileNotFoundError:
            return [0,[]]
    except json.decoder.JSONDecodeError:
            return [0,[]]

"""
This Function Writes the json file with latest list 
"""
def save_database(database, identity_id):
    with open(DB_PATH,"w") as f:
        database = [identity_id,list(map(asdict, database))]
        json.dump(database, f, indent=4)
    return True

# This is the Service class which handles CRUD Operations
class TaskService:
    def displayTasks(status=""):
        unique_id,database = load_database()
        tasks = []
        if status != "" and status in ["todo", "done", "in-progress"]:
            for task in database:
                if (task.status==status):
                    tasks.append(task)
        else:
            tasks = database

        print(tabulate(tasks, headers="keys", tablefmt="rounded_outline"))

    def addTask(task_description):
        try:
            unique_id,database =load_database()
            task = Task(unique_id+1,task_description,"todo",datetime.now().strftime("%Y-%m-%d %H:%M:%S"), datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            database.append(task)
            save_database(database,unique_id+1)
            return True
        except Exception as e:
            print(f"Failed to add the task error message {e}")

    def removeTask(id):
        try:
            unique_id,database = load_database()
            database = [task for task in database if task.id != id]
            save_database(database, unique_id)
            return True
        except Exception as e:
            print(f"Failed to remove the task error message {e}")

    def updateTask(id, description="", status=""):
        try:
            unique_id,database=load_database()
            if (status.lower() not in ["todo", "in-progress", "done", ""]):
                raise Exception(f"{status} is not a valid status")
            for task in database:
                if (task.id == id):
                    task.description = description if description!="" else task.description
                    task.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    task.status = status if status!="" else task.status
                    break
            save_database(database, unique_id)
            return True
        except Exception as e:
            print(f"Failed to update the task error message {e}")













