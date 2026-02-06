
---

# Task Tracker CLI

A simple command line tool to manage daily tasks.
It allows you to add, update, remove, and display tasks directly from your terminal.

## Features

* Add new tasks
* Update task status or description
* Remove tasks
* Display all tasks
* Filter tasks by status

## Installation

Clone the repository:

```bash
git clone https://github.com/N092/Task-Tracker-CLI.git
cd Task-Tracker-CLI
```

Make sure Python 3 is installed:

```bash
python --version
```

## Usage

Run the CLI using:

```bash
python task-cli.py <command> [arguments]
```

### Add a task

```bash
python cli.py add "Complete DSA practice"
```

### Update a task

Update status:

```bash
python cli.py update 1 --status "done"
```

Update description:

```bash
python cli.py update 1 --description "Revise Python argparse"
```

Update both:

```bash
python cli.py update 1 --status "in-progress" --description "Work on CLI project"
```

### Remove a task

```bash
python cli.py remove 1
```

### Display tasks

Display all tasks:

```bash
python cli.py display
```

Filter by status:

```bash
python cli.py display --status "done"
python cli.py display --status "in-progress"
python cli.py display --status "todo"
```

## Project Structure

```
Task-Tracker-CLI/
│
├── task-cli.py
├── services.py
├── models.py
└── task_database.json
```

* `task-cli.py` handles command line arguments
* `services.py` contains business logic
* `models.py` defines the Task structure
* `task_database.json` stores task data

## Requirements

* Python 3.8 or higher

## Notes

This project is built as a lightweight learning exercise to understand CLI design, argument parsing, and basic project structure in Python.

---
