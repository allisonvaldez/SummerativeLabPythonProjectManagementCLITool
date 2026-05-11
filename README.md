# Python Project Management CLI Tool

A command-line interface tool for managing users, projects, and tasks.

## Setup

```bash
pip install -r requirements.txt
```

## How to Run

```bash
# Add a user
python3 main.py add-user --name "Allison" --email "allison@email.com"

# Add a project
python3 main.py add-project --user "Alice" --title "CLI Tool" --description "My project" --due-date "2026-12-01"

# Add a task
python3 main.py add-task --project "CLI Tool" --title "Write tests" --assigned-to "Alice"

# List users
python3 main.py list-users

# List projects
python3 main.py list-projects --user "Alice"

# List tasks
python3 main.py list-tasks --project "CLI Tool"

# Complete a task
python3 main.py complete-task --title "Write tests"
```

## Features

- Create and manage users, projects, and tasks
- One-to-many relationships: User → Projects → Tasks
- JSON file persistence
- Pretty table output using rich
- Input validation with error messages

## Project Structure

```
main.py          — CLI entry point
models/          — User, Project, Task classes
utils/           — File IO and display helpers
data/            — JSON storage files
testing/         — Unit tests
requirements.txt — Dependencies
```