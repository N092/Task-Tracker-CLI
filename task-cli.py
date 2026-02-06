from model import Task
from service import TaskService, load_database, save_database
import argparse
import json

def main():
    service = TaskService

    parser = argparse.ArgumentParser(
        prog='task',
        description='A Command Line tool to manage all the tasks'
    )

    subparsers = parser.add_subparsers(dest="command")

    # ADD
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # REMOVE
    remove_parser = subparsers.add_parser("delete", help="delete a task")
    remove_parser.add_argument("id", type=int, help="id of the task to be removed")

    # UPDATE
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("id", type=int, help="id of the task to be updated")
    update_parser.add_argument("--status", type=str, help="New status")
    update_parser.add_argument("--description", type=str, help="New description")

    # DISPLAY
    display_parser = subparsers.add_parser("list")
    display_parser.add_argument(
        "--status",
        choices=["todo", "in-progress", "done"],
        help="Filter by status"
    )

    args = parser.parse_args()

    if args.command == "add":
        service.addTask(args.description)
        print(f"Task added successfully (ID: {args.id})")

    elif args.command == "delete":
        service.removeTask(args.id)
        print(f"Task removed with ID: {args.id}")

    elif args.command == "update":
        service.updateTask(
            args.id,
            status=args.status if args.status else "",
            description=args.description if args.description else ""
        )
        print(f"Task updated with ID: {args.id}")


    elif args.command == "list":
        service.displayTasks(status=args.status)

if __name__ == "task-cli":
    main()
