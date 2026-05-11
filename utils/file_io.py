# Needed for File IO its responsible for saving and loading data to and from the JSON files
import json
import os

# Create a function to save the data
def save_data(filepath, data):
    # Save the list of dictionaries to the JSON file
    try:
        # Open the file in write mode and place the data as formatted JSON
        with open()filepath, "w") as f:
            json.dump(data, f, indent=4)
    except:
        # Perform error handling 
        print(f"Error saving data: {e}")

# Create a function to load the data
def load_data(filepath):
    # Load the data from the JSON file and return empty if no file
    try:
        # Perform error handling to check if the file is there 
        if not os.path.exists(filepath):
            return []
        with open(filepath, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, Exception) as e:
          print(f"Error loading data: {e}")
          return []

# Create a function to save the data
def save_all(users, projects, tasks):
    save_data("data/users.json", [u.to_dict() for u in users])
    save_data("data/projects.json", [p.to_dict() for p in projects])
    save_data("data/tasks.json", [t.to_dict() for t in tasks])