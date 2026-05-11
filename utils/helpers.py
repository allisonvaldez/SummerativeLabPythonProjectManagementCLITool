# Needed for helper utils its needed for formatting and display functions properly
from rich.table import Table
from rich.console import Console

# Create instance for rich output
console = Console()

# Create a function to print users
def print_users(users):
    # Create a table
    table = Table(title="Users")
    # Add columns
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Email", style="yellow")
    # Place users
    for user in users:
        table.add_row(str(user.id), user.name, user.email)
    console.print(table)

# Create a function to print projects
def print_prjects(projects):
    # Create a table
    table = Table(title="Projects")
    # Add columns
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Description", style="white")
    table.add_column("Due Date", style="yellow")
    table.add_column("Owner", style="magenta")
    # Place projects
    for project in projects:
        table.add_row(
            str(project.id),
            project.title,
            project.description,
            project.due_date,
            project.user.name
            )
    console.print(table)


# Create a function to print tasks
def print_prjects(projects):
    # Create a table
    table = Table(title="Projects")
    # Add columns
    table = Table(title="Tasks")
    table.add_column("ID", style="cyan")
    table.add_column("Title", style="green")
    table.add_column("Status", style="yellow")
    table.add_column("Assigned To", style="magenta")
    table.add_column("Project", style="white")
    # Place tasks
    for project in projects:
        table.add_row(
            str(task.id),
            task.title,
            task.status,
            task.assigned_to,
            task.project.title
            )
    console.print(table)
