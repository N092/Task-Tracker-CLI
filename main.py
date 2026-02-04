from dataclasses import asdict
from datetime import datetime

from model import Task
from service import TaskService, load_database, save_database
import argparse

if __name__ == "__main__":
    task = TaskService
    task.addTask("Study for tommorow Exam")
    task.displayAllTask()

