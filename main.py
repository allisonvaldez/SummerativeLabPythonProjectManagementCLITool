#!/usr/bin/env python3

# This is the main.py file MUST use argparse to define all commands
import argparse
from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import save_all
from utils.helpers import print_users, print_projects, print_tasks

# Create a function to add user 
def add_user(args):
    # Perform error handling
    if User.find_by_name(args.name):
        print(f"Sorry, the user '{args.name}' already exists.")
        return
    
    # Create user instance
    user = User(args.name, args.email)

    # Save data to JSON file
    save_all(User.all, Project.all, Task.all)
    print(f"Congradulations, user '{user.name}' was created.")

# Create a function to list users
def list_users(args):
    # Perform error handling
    if not User.all:
        print("No users found.")
        return
    print_users(User.all)

# Create a function to add a project to a user
def add_project(args):
    # First find the proper user
    user = User.find_by_name(args.user)

    # Perform error handling
    if not user:
        print(f"Sorry, user '{args.user}' was not found.")
        return
    
    # Create project instance
    project = Project(args.title, args.description, args.due_date, user)
    save_all(User.all, Project.all, Task.all)
    print(f"Congradulations, project '{project.title}' added to {user.name}.")

# Create a project list for a user
def list_projects(args):

    # Select user
    if args.user:
        # Find proper user
        user = User.find_by_name(args.user)

        # Perform error handling
        if not user:
            print(f"Sorry, user '{args.user}' was not found.")
            return
        projects = Project.find_by_user(user)

    else:
        projects = Project.all
    # Error handling
    if not projects:
        print("No projects found.")
        return
    print_projects(projects)

# Create a function to add tasks to a project
def add_task(args):

    # Find the proper project by name/title
    project = Project.find_by_title(args.project)

    # Perform error handling
    if not project:
        print(f"Sorry, project '{args.project}' was not found.")
        return
    
    # Create task instance
    task = Task(args.title, args.assigned_to, project)
    save_all(User.all, Project.all, Task.all)
    print(f"Awesome, '{task.title}' added to project '{project.title}'.")

# List tasks for projects
def list_tasks(args):

    # If theres a project
    if args.project:
        # Find project and tasks
        project = Project.find_by_title(args.project)
        # Error handling
        if not project:
            print(f"Sorry, project '{args.project}' was not found.")
            return
        tasks = Task.find_by_project(project)

    else:
        tasks = Task.all

    # Error handling
    if not tasks:
        print("No tasks found.")
        return
    print_tasks(tasks)

# Create a function to complete tasks
def complete_task(args):
    # Find the task
    task = Task.find_by_title(args.title)
    # Perform error handling
    if not task:
        print(f"Sorry, task '{args.title}' not found.")
        return
    task.complete()
    save_all(User.all, Project.all, Task.all)


def main():
    # Create main parser
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(title="commands")

    # Need add-user command
    p = subparsers.add_parser("add-user", help="Add a new user")
    p.add_argument("--name", required=True, help="User's name")
    p.add_argument("--email", required=True, help="User's email")
    p.set_defaults(func=add_user)

    # Need list-users command
    p = subparsers.add_parser("list-users", help="List all users")
    p.set_defaults(func=list_users)

    # Need add-project command
    p = subparsers.add_parser("add-project", help="Add a project to a user")
    p.add_argument("--user", required=True, help="User's name")
    p.add_argument("--title", required=True, help="Project title")
    p.add_argument("--description", default="", help="Project description")
    p.add_argument("--due-date", dest="due_date", default="TBD", help="Due date")
    p.set_defaults(func=add_project)

    # Need list-projects command
    p = subparsers.add_parser("list-projects", help="List all projects")
    p.add_argument("--user", default=None, help="Filter by user name")
    p.set_defaults(func=list_projects)

    # Need add-task command
    p = subparsers.add_parser("add-task", help="Add a task to a project")
    p.add_argument("--project", required=True, help="Project title")
    p.add_argument("--title", required=True, help="Task title")
    p.add_argument("--assigned-to", dest="assigned_to", default="Unassigned", help="Assigned to")
    p.set_defaults(func=add_task)

    # Need list-tasks command
    p = subparsers.add_parser("list-tasks", help="List all tasks")
    p.add_argument("--project", default=None, help="Filter by project title")
    p.set_defaults(func=list_tasks)

    # Need complete-task command
    p = subparsers.add_parser("complete-task", help="Mark a task as complete")
    p.add_argument("--title", required=True, help="Task title")
    p.set_defaults(func=complete_task)

    # Parse arguments and call functions
    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        # Provide help
        parser.print_help()

if __name__ == "__main__":
    main()