# Include tests for User, Project, and Task models
import pytest
from models.user import User
from models.project import Project
from models.task import Task

# Reset class state before each test to avoid cross-test contamination
@pytest.fixture(autouse=True)
def reset_state():
    User.all = []
    User.id_counter = 1
    Project.all = []
    Project.id_counter = 1
    Task.all = []
    Task.id_counter = 1

# Test if user initializes with name and email
def test_user_init():
    user = User("Allison", "allison@email.com")
    assert user.name == "Allison"
    assert user.email == "allison@email.com"

# Test if user provides invalid email
def test_user_invalid_email():
    with pytest.raises(ValueError):
        User("Allison", "notanemail")

# Test if can find user by name
def test_user_find_by_name():
    user = User("Allison", "allison@email.com")
    assert User.find_by_name("Allison") == user

# Test if project initializes and links to user
def test_project_init():
    user = User("Allison", "allison@email.com")
    project = Project("CLI Tool", "A CLI project", "2026-12-01", user)
    assert project.title == "CLI Tool"
    assert project.user == user
    assert project in user.projects

# Test if task initializes and links to project
def test_task_init():
    user = User("Allison", "allison@email.com")
    project = Project("CLI Tool", "A CLI project", "2026-12-01", user)
    task = Task("Write tests", "Alice", project)
    assert task.title == "Write tests"
    assert task.status == "pending"
    assert task in project.tasks

# Test if task complete method updates its status
def test_task_complete():
    user = User("Allison", "allison@email.com")
    project = Project("CLI Tool", "A CLI project", "2026-12-01", user)
    task = Task("Write tests", "Alice", project)
    task.complete()
    assert task.status == "complete"