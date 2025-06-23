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

task_tags = ["Title", "Description", "Assignee", "Priority"]

def integer_validation(input_value, min_value, max_value):
    try:
        input_value = int(input_value)
        if input_value <= min_value -1:
            return (f"Please Choose a number between {min_value} and {max_value}!")
        elif input_value >= max_value +1:
            return f"Please Choose a number between {min_value} and {max_value}!"
        else:
            return True
    except:
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

def generate_task_id():
    number_of_tasks = len(tasks)
    task_id = f"T{number_of_tasks}"
    return task_id

def check_multiple_user_values(user_input_values):
    if user_input_values != None:
        for singular_value in user_input_values:
            if singular_value == "":
                easygui.msgbox("Error! You need to fill in all values!")
                create_new_task()
                return
        return True
    else:
        easygui.msgbox("No Values input. Returning to homepage.")

def input_multiple_values(values_to_enter, title):
    box_msg = f"Please input the info to {title}"
    box_title = title
    user_input_values = easygui.multenterbox(box_msg,box_title,values_to_enter)
    checked_values = check_multiple_user_values(user_input_values)
    if checked_values == False:
        check_multiple_user_values()
    elif checked_values == True:
        return user_input_values

def create_new_task():
    min_value = 1
    max_value = 3
    user_input = input_multiple_values(values_to_enter=task_tags, title="Create a New Task")
    print(user_input)
    new_task = {
        "Title": user_input[0],
        "Description": user_input[1],
        "Assignee": user_input[2],
        "Priority": user_input[3],
        "Status": "Not Started"
    }
    for field in new_task:
        if field == "Priority":
            value = integer_validation(user_input[3], min_value,max_value)
            if value != True:
                easygui.msgbox(f"{value}", "Error")
            else:
                task_id = generate_task_id()
                tasks[task_id] = new_task
                print(tasks)


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
        box_msg = "Welcome to the Task Manager! Please choose your option."
        box_title = "Task Manager - Home"
        choices = []
        for action in options:
            choices.append(action)
        
        selection = easygui.buttonbox(box_msg,box_title,choices)
        if selection is None:
            selection = "Exit"
        
        get_input = options[selection]()
        
user_menu(tasks, team_members)