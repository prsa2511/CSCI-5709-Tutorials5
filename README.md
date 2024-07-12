# Tutorial 5

This project is a Flask-based web application designed to handle user data with APIs for adding, updating, retrieving a list of users, and retrieving a specific user by ID.

* *Date Created*: 12 July 2024
* *Last Modification Date*: 12 July 2024
* *Lab URL*: <https://csci-5709-tutorials5.onrender.com>
* *Git Individual URL*: <https://git.cs.dal.ca/psakaria/csci-5709-tutorial5>
* *Git URL*: <https://git.cs.dal.ca/psakaria/csci-5709-tutorials/-/tree/main/Tutorial5?ref_type=heads>

## Authors

* [Pratik Sakaria](pratik.sakaria@dal.ca)

## Getting Started

This section provides instructions on setting up the project locally. To get a local copy up and running follow these simple steps.

### Prerequisites

Before running this project, you need to install the following software / libraries / plug-ins

```
Python 3.x (https://www.python.org/)
pip (comes with Python)

```
See the following section for detailed step-by-step instructions on how to install this software / libraries / plug-ins


### Installing

A step by step series of examples that tell you how to get a development env running

1. Clone the repository:

```
git clone <repository_url>
cd <repository_name>
```

2. Set up the Flask environment:

```
python app.py

```

## Built With

* [Flask](https://flask.palletsprojects.com/en/3.0.x/) The web framework used

## Sources Used

If in completing your lab / assignment / project you used any interpretation of someone else's code, then provide a list of where the code was implemented, how it was implemented, why it was implemented, and how it was modified. See the sections below for more details.


### app.py

*Lines 3 - 15*
```
class User:
    def __init__(self, username, email):
        self.id = str(len(listOfUsers) + 1)  # Automatically assign an ID based on the list length
        self.username = username
        self.email = email

listOfUsers = []

user1 = User("user1", "user1@gmail.com")
user2 = User("user2", "user2@gmail.com")

listOfUsers.append(user1)
listOfUsers.append(user2)
```
The code above was inspired by general Python class usage and list management as demonstrated in multiple online Python tutorials.

- <!---How---> The code was implemented by defining a User class and a list to store user objects.
- <!---Why---> This approach was used to simulate a simple in-memory database for user management.
- <!---How---> The code was modified to dynamically assign user IDs based on the list length, ensuring unique IDs.


## Acknowledgments

* Thanks to Flask documentation for guidance on Flask application development.
