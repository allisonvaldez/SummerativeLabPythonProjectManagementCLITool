# Task model dictactes what task assigned to a project

# Class for Task
class Task:
    #  Provide a level counter and provide a list to store
    id_counter = 1
    all = []

    # Constructor
    def __init__(self, title, assigned_to, project):
        self.title = title
        # Make sure status is automatically set to "pending" upon creation
        self.status = "pending"
        self.assigned_to = assigned_to
        self.project = project
        # Unique id needs to be linked to the counter
        self.id = Task.id_counter
        Task.id_counter += 1
        # Place task at the class level for the list
        Task.all.append(self)
        # Add project to the user project running list
        project.add_task(self)
    
    # Create a function for when a task is completed and print a confirmation message
    def complete(self):
        self.status = "complete"
        print(f"Task '{self.title}' marked as complete.")

    # Create a class method
    @classmethod
    # Create a function to find a task by name/title 
    def find_by_title(cls, title):
        # Return none if not found
        for task in cls.all:
            if task.title == title:
                return task
        return None
    
    # Create a method
    @classmethod
    # Create a function to find task by project
    def find_by_project(cls, project):
        return [t for t in cls.all if t.project == project]

    # Create a function to convert data for JSON
    def to_dict(self):
        # Convert task to dictionary for JSON storage
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project": self.project.title
        }
    
    # Create a function to manipulate how data is viewed when printed
    def __repr__(self):
        # Clean string representation for CLI output
        return f"Task #{self.id}: {self.title} | Status: {self.status} | Assigned to: {self.assigned_to}"