# User model it should inherit from Person class

# Class for Person
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        # For CLI output
        return f"{self.name} ({self.email})"

# Class for User
class User(Person):
    # Class level counter and provide a list to store
    id_counter = 1
    all = []

    # Contructor
    def __init__(self, name, email):
        # Need a parent class contructure delegation
        super().__init__(name, email)
        # Unique id needs to be linked to the counter
        self.id = User.id_counter
        User.id_counter += 1
        # Create an list of project for users
        self.projects = []
        # Place user at the class level for the list
        User.all.append(self)
    
    # Create a property
    @property
    # Create a function for user name
    def name(self):
        # Getter
        return self.name
    
    # Create function and setter for name
    @name.setter
    def name(self, value):
        # Perform error handling for nonempty strings
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Sorry, please provide a nonempty string!")
        self._name = value
    
    # Create a property
    @property
    # Create a function for email
    def email(self):
        # Getter
        return self._email
    
    # Create function and setter for email
    @email.setter
    def email(self, value):
        # Perform error handling to check if it contains "@"
        if not isinstance(value, str) or "@" not in value:
            raise ValueError("Sorry, please provide a valid email address!")
        self._email = value
    
    # Create a function to add projects
    def add_project(self, project):
        self.projects.append(project)
    
    # Create a function to gather projects of user
    def get_projects(self):
        return self.projects
    
    # Create a classmethod
    @classmethod
    @name.setter
    # Create a function to search for a user
    def find_user(cls, name):
        for user in cls.all:
            if user.name == name:
                return user
            return None
    
    # Create a function to convert data for JSON
    def convert_dict_to_JSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }
    
    # Create a function to manipulate how data is viewed when printed
    def __repr__(self):
        # Clean string representation for CLI output
        return f"User #{self.id}: {self.name} | {self.email}"