import easygui

task_list = { #Dictionaries
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

#Validation.

def string_validation(user_input):
    box_title = "Error"
    box_message = "Error! You need to fill in all values!"
    if type(user_input) == list:
        if user_input != None:
            for singular_value in user_input:
                if singular_value == "":
                    easygui.msgbox(box_message, box_title)
                    return "missing"
            return True
        else:
            easygui.msgbox("No Values input. Returning to homepage.")
    else:
        if user_input == None or len(user_input) == 0:
            easygui.msgbox("No Values input. Returning to homepage.")
            return
        else:
            return True


def integer_validation(user_input, min_value, max_value):
    try:
        user_input = int(user_input)
        if user_input <= min_value -1:
            return f"Please Choose a number between {min_value} and {max_value}!"
        elif user_input >= max_value +1:
            return f"Please Choose a number between {min_value} and {max_value}!"
        else:
            return True
    except:
        return "Please input a number!"




#Functions used for searching both tasks and users.

def search_selection():
    options = {
        "Search for a Team Member": search_members,
        "Search for a Task": search_tasks,
        "Cancel": exit,
    }
    box_msg = "Please select what you would like to search!"
    box_title = "Task Manager - Search"
    choices = []
    for action in options:
        choices.append(action)

    selection = easygui.buttonbox(box_msg,box_title,choices)
    if selection == None or selection == "Cancel":
        return    
    options[selection]()

def search_tasks():
    choices = []
    for task_id in task_list:
        for key in task_list[task_id]:
            if key == "Title":
                choices.append(f"{task_id}. {task_list[task_id]['Title']}")
    box_msg = "What task would you like to view?"
    box_title = "Task Manager - Search"
    choice = easygui.choicebox(box_msg, box_title, choices)
    print(choice)
    #Link to output function

def search_members():
    user_input = search_members_input()
    if user_input == "homepage":
        return
    else:
        member_exists = search_members_dictionary(user_input)
        if member_exists == True:
            easygui.msgbox(f"User found! {user_input}")
        else:
            easygui.msgbox("Error: Member does not exist!")

            
def search_members_dictionary(user_input):
    for member_id in team_members:
        if member_id.lower() == user_input.lower():
            return True
        else:
            for member_value in team_members[member_id]:
                if member_value == "Name":
                    if team_members[member_id][member_value].lower() == user_input.lower():
                        print(team_members[member_id][member_value])
                        return True #output from here

def search_members_input():
    box_title = "Task Manager - Search"
    box_msg = "Enter the team member's name or ID."
    user_input = easygui.enterbox(box_msg, box_title)
    validation = string_validation(user_input)
    if validation == True:
        return user_input
    else:
        return "homepage"

    
#Functions for outputting.

def generate_report():
    pass

def output_tasks():
    pass


#Functions used for updating Tasks.

def update_task():
    pass




#Functions used for adding Tasks.

def generate_task_id():
    number_of_tasks = len(task_list) + 1
    task_id = f"T{number_of_tasks}"
    return task_id



def input_multiple_values(values_to_enter, title):
    box_msg = f"Please input the info to {title}"
    box_title = title
    user_input = easygui.multenterbox(box_msg,box_title,values_to_enter)
    checked_values = string_validation(user_input)
    if checked_values == True:
        return user_input
    elif checked_values == "missing":
        create_new_task()

def create_new_task():
    min_value = 1
    max_value = 3
    user_input = input_multiple_values(values_to_enter=task_tags, title="Task Manager - Create a New Task")
    if user_input == None:
        return
    else:
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
                    create_new_task()
                else:
                    task_id = generate_task_id()
                    task_list[task_id] = new_task
                    print(task_list)


def user_menu():
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
        
user_menu()