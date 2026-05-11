# Project model dictates what project is assigned to a user

# Class for Project
class Project:
    #  Provide a level counter and provide a list to store
    id_counter = 1
    all = []

    # Constructor
    def __init__(self, title, description, due_date, user):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user = user
        # Unique id needs to be linked to the counter
        self.id = Project.id_counter
        Project.id_counter += 1
        self.task = []
        # Place project at the class level for the list
        Project.all.append(self)
        # Add project to the user project running list
        user.add_project(self)

    # Create a property
    @property
    # Create a function for title of project
    def title(self):
        # Getter
        return self._title
    
    # Create function and setter for title
    @title.setter
    def title(self, value):
        # Perform error handling for nonempty strings
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Sorry, please provide a nonempty string!")
        self._title = value

    # Create a function to add tasks
    def add_task(self, task):
        self.task.append(task)

    # Create a function to get said tasks
    def get_tasks(self):
        self.task

    # Create a class method
    @classmethod
    # Create a function to find project title
    def find_by_title(cls, title):
        # Search for the title return none if it isn't found
        for project in cls.all:
            if project.title == title:
                return project
            return None
    
    # Create a class method
    @classmethod
    # Create a function to find projects by user's name
    def find_by_username(cls, user):
        # Return projects by user
        return [p for p in cls.all if p.user == user]
    
    # Create a function to convert data for JSON
    def convert_dict_to_JSON(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user": self.user.name
        }

    # Create a function to manipulate how data is viewed when printed
    def __repr__(self):
        return f"Project #{self.id}: {self.title} | Due: {self.due_date} | Owner: {self.user.name}"

