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

task_tags = ["Title", "Description", "Priority"]

#Validation.

def string_validation(user_input):
    box_title = "Error"
    box_message = "Error! You need to fill in all values!"
    if type(user_input) == list:
        if user_input != None:
            user_input_iteration = 0
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
    box_msg = "What task would you like to view or update?"
    box_title = "Task Manager - Search"
    choice = easygui.choicebox(box_msg, box_title, choices)
    if choice != None:
        task_id = choice.split(".")
    else:
        return
    output_task(task_id[0])

def search_members():
    user_input = search_members_input()
    if user_input == "homepage":
        return
    else:
        member_exists = search_members_dictionary(user_input)
        if member_exists == True:
            user_id = user_input
            output_user(user_id)
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
                        return True

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

def output_user(user_id):
    output = [f"--- {user_id}. {team_members[user_id]['Name']} ---"]
    for key, value in team_members[user_id].items():
        if key == 'Assigned Tasks':
            output.append("Assigned Tasks:")
            for assigned_task in value:
                output.append(f"- {assigned_task}. {task_list[assigned_task]['Title']}")
        else:
            output.append(f"{key}: {value}")
    easygui.msgbox("\n".join(output), title=team_members[user_id]["Name"])
    
def output_task(task_id):
    
    options = {
        "Assign Task to a User": assign_task_selector,
        "Edit Task": update_task, 
        "Cancel": exit
    }
    output = [f"--- {task_id}. {task_list[task_id]['Title']} ---"]
    for key, value in task_list[task_id].items():
        output.append(f"{key}: {value}")

    choices = []
    for action in options:
        choices.append(action)

    selection = easygui.buttonbox("\n".join(output), title=task_list[task_id]["Title"], choices=choices)
    if selection == None or selection == "Cancel":
        return
    elif selection == "Assign Task to a User":
        assign_task_selector(task_id)
    else:    
        options[selection]()


def output_all_tasks():
    output = []
    for task_id, task in task_list.items():
        output.append(f"--- {task_id}. {task['Title']} ---")
        for key, value in task.items():
            if key != "Title":
                output.append(f"{key}: {value}")
        output.append("")
    easygui.msgbox("\n".join(output), title="All Tasks")


#Functions used for updating Tasks.

def update_task(task_id):
    pass
    task = task_list[task_id]
    editable_fields = [field for field in task_tags]
    box_msg = "Which Field would you like to edit?"
    box_title = "Task Manager - Edit Task"
    field_to_edit = easygui.buttonbox(box_msg, box_title, editable_fields)

    if not field_to_edit:
        easygui.msgbox("No Field Selected. Edit Cancelled.")
        return
    if field_to_edit in ["Priority"]:
        pass

def assign_task_selector(task_id):
    box_msg = f"What member would you like to assign: \n{task_id}. {task_list[task_id]['Title']}"
    box_title = "Task Manager - Assigning a Task"
    choices = []
    for member_id in team_members:
        for key in team_members[member_id]:
            if key == "Name":
                choices.append(f"{member_id}. {team_members[member_id]['Name']}")
    choice = easygui.choicebox(box_msg, box_title, choices)
    if choice != None:
        user_id = choice.split(".")
    else:
        return
    check_if_user_already_has_task(user_id[0], task_id)

def check_if_user_already_has_task(user_id, task_id):
    loop_iteration = 0
    for assigned_task in team_members[user_id]['Assigned Tasks']:
        loop_iteration += 1
        if loop_iteration != len(team_members[user_id]['Assigned Tasks']):
            if task_id == assigned_task:
                box_title = "Task Manager - Error"
                box_msg = f"Error: User '{team_members[user_id]['Name']}' already has task '{task_list[task_id]['Title']}' assigned to them!"
                easygui.msgbox(box_msg, box_title)
                return
            else:
                loop_iteration += 1

    if loop_iteration == len(team_members[user_id]['Assigned Tasks']):
        assign_task(task_id, user_id)

def assign_task(task_id, user_id):
    team_members[user_id]['Assigned Tasks'].append(task_id)
    print(team_members[user_id]['Assigned Tasks'])
    return

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
            "Assignee": "None",
            "Priority": user_input[2],
            "Status": "Not Started"
        }
        for field in new_task:
            if field == "Priority":
                value = integer_validation(user_input[2], min_value,max_value)
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
        "Update a Task": search_tasks,
        "Search for a Task or Team Member": search_selection,
        "Generate a Report": generate_report,
        "Show all Tasks": output_all_tasks,
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