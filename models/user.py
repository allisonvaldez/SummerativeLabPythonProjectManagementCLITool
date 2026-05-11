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
    #