import easygui

tasks = { #Dictionaries
    "T1": {
        "Title": "Design Homepage",
        "Description": "Create a Mockup of the Homepage",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "In Progress"
    },
    "T2": {
        "Title": "Implement Login Page",
        "Description": "Create the Login page for the website",
        "Assignee": "JSM",
        "Priority": 3,
        "Status": "Blocked"
    },
    "T3": {
        "Title": "Fix Navigation Menu",
        "Description": "Fix the navigation menu to be more user-friendly",
        "Assignee": "None",
        "Priority": 1,
        "Status": "Not Started"
    },
    "T4": {
        "Title": "Add Payment processing",
        "Description": "Implement payment processing for the website",
        "Assignee": "JLO",
        "Priority": 2,
        "Status": "In Progress"
    },
    "T5": {
        "Title": "Create an About Us Page",
        "Description": "Create a page with information about the company",
        "Assignee": "BDI",
        "Priority": 1,
        "Status": "Blocked"
    },
}

team_members = {
    "JSM": {
        "Name": "John Smith",
        "Email": "John@techvision.com",
        "Assigned Tasks": ["T1", "T2"]
    },
    "JLO": {
        "Name": "Jane Love",
        "Email": "Jane@techvision.com",
        "Assigned Tasks": ["T4"]
    },
    "BDI": {
        "Name": "Bob Dillon",
        "Email": "Bob@techvision.com",
        "Assigned Tasks": ["T5"]
    },
}

task_tags = ["Title", "Description", "Priority"]

def integer_validation(input_value, min_value, max_value):
    if type(input_value) == int:
        if input_value <= min_value -1:
            return (f"Please Choose a number between {min_value} and {max_value}!")
        elif input_value >= max_value +1:
            return f"Please Choose a number between {min_value} and {max_value}!"
        else:
            return True
    else:
        return "Please input a number!"



def update_task():
    pass

def search_selection():
    pass

def search_tasks():
    pass

def search_members():
    pass

def generate_report():
    pass

def output_tasks():
    pass

def input_values(task_tags):

def create_new_task(task_tags):
    task_values = []
    new_task = {}
    easygui.msgbox("You are now adding a New Task.", "New Task")
    input_values()
    for field in task_tags:
        if field.lower() in ["Priority"]:
            value = integer_validation()
            if value != True:
                easygui.msgbox(f"{value}", "Error")
            else:
                easygui.msgbox("Your input is valid")

def user_menu(tasks, team_members):
    options = {
        "Add a New Task": create_new_task,
        "Update a Task": update_task,
        "Search for a Task or Team Member": search_selection,
        "Generate a Report": generate_report,
        "Show all Tasks": output_tasks,
        "Exit": exit,
    }
    get_input = None
    while get_input != "Exit":
        msg = "Welcome to the Task Manager! Please choose your option."
        title = "Task Manager - Home"
        choices = []
        for action in options:
            choices.append(action)
        
        selection = easygui.buttonbox(msg,title,choices)
        if selection is None:
            selection = "Exit"
        
        get_input = options[selection]()
        
user_menu(tasks, team_members)