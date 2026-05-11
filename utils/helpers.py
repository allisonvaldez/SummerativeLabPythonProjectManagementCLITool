# Helper utilities — formatting and display functions using rich
from rich.table import Table
from rich.console import Console

# Create a console instance for rich output
console = Console()

def print_users(users):
    """Display users in a formatted table using rich"""
    # Create a table with columns
    table = Table(title="Users")
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Email", style="yellow")
    # Add each user as a row
    for user in users:
        table.add_row(str(user.id), user.name, user.email)
    console.print(table)

def print_projects(projects):
    """Display projects in a formatted table using rich"""
    table = Table(title="Projects")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Description", style="white")
    table.add_column("Due Date", style="yellow")
    table.add_column("Owner", style="magenta")
    # Add each project as a row
    for project in projects:
        table.add_row(
            str(project.id),
            project.title,
            project.description,
            project.due_date,
            project.user.name
        )
    console.print(table)

def print_tasks(tasks):
    """Display tasks in a formatted table using rich"""
    table = Table(title="Tasks")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Status", style="yellow")
    table.add_column("Assigned To", style="magenta")
    table.add_column("Project", style="white")
    # Add each task as a row
    for task in tasks:
        table.add_row(
            str(task.id),
            task.title,
            task.status,
            task.assigned_to,
            task.project.title
        )
    console.print(table)