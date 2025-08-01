import easygui

# Dictionary containing all the tasks.
task_list = { 
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

# Dictionary of all the team members
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

# Items which are editable in the program, which usually show up as
# buttons in button-boxes while creating or editing a task.
# extra_editable_task_tags are in a seperate list because they are not
# initally ascociated with task creation, only set later on.
task_tags = ["Title", "Description","Priority"]
extra_editable_task_tags = ["Status", "Assignee"]
status_options = ["In Progress", "Not Started", "Blocked", "Complete"] 


#Functions which focus on validating user input.

def string_validation(user_input):
    '''
    Checks if the value that the user input has anything missing, like
    if the user has not filled in some values.
    Returns:
        - True if the string is valid and no values are missing.
        - "missing" if any of the inputs are missing, along with an 
        error message.
    '''
    box_title = "Error"
    box_message = "Error! You need to fill in all values!"
    # Handles Validation if the input is sent from a 
    # multi-enter box (list) type.
    if type(user_input) == list:
        if user_input != None:
            for looped_user_input in user_input:
                if looped_user_input == "":
                    easygui.msgbox(box_message, box_title)
                    return "missing"
            return True
    # Handles Validation if the input is sent from a enter box 
    # (string) type.
    else:
        if user_input != None:
            return True


def integer_validation(user_input, min_priority, max_priority):
    '''
    Checks if the user has input an integer, and if the integer fits 
    withing the minimum and maximum values set by the function.
    Returns:
        - True if the user input is valid (is an integer and falls 
        between the minimum and maximum range.)
        - Please Choose a number between {min_priority} and 
        {max_priority}!" is if the user input a number which is not
        inbetween the minimum and maximum range
        - "Please input a number!" if the user input a string or other
        types of data types.
    '''
    try:
        # Checks if the user input an integer.
        # Then if it did, compares the integer with the set minimum and
        # maximum values.
        user_input = int(user_input)
        if user_input <= min_priority -1 or user_input >= \
        max_priority +1:
            return (f"Please Choose a number between {min_priority} " +
            f"and {max_priority}!")
        else:
            return True
    except:
        return "Please input a number for priority!"

#Functions used for searching for both tasks and users.

def search_selection():
    '''
    Creates a menu with 2 buttons, allowing the user to choose what to
    search for: either for tasks or for users.
    '''
    options = {
        "Search for a Team Member": search_members,
        "Search for a Task": pre_search_tasks,
        "Cancel": exit,
    }
    box_msg = "Please select what you would like to search!"
    box_title = "Task Manager - Search"
    choices = []
    # This loop loops through the options dictionary that was defined
    # above and adds the title of the title to a button in the button
    # box. Then, when an option is selected, it runs the function (key)
    # ascociated with the title.
    for action in options:
        choices.append(action)

    selection = easygui.buttonbox(box_msg,box_title,choices)
    if selection == None or selection == "Cancel":
        return
    options[selection]()


def pre_search_tasks():
    '''
    This function allows the program to run an input through the search
    function, allowing it to specify that it is searching for a task to
    output, and not a task to edit, as there is no way to have the
    brackets with the menu, making this function necessary.
    '''
    user_input = search_tasks("Search")
    if user_input == False:
        return


def search_tasks(reason_for_search):
    '''
    This function loops through the task dictionary, grabbing the task
    ID and task name and puts them together to create a nice choice box
    with all the tasks, which the user can choose from.
    It also leads the program to output or edit the selected task.
    '''
    choices = []
    # This loop loops through the task list, grabbing both the ID and
    # title of each task, appending it to be displayed in a list the
    # user can choose from.
    for task_id in task_list:
        for key in task_list[task_id]:
            if key == "Title":
               choices.append(f"{task_id}. {task_list[task_id]['Title']}")
    box_msg = f"What task would you like to {reason_for_search}?"
    box_title = "Task Manager - Search"
    user_input = easygui.choicebox(box_msg, box_title, choices)
    if user_input != None:
        # Splits the task ID from the combined display name with ID, and
        # only running the ID through the functions listed below, as
        # the input is displayed as 'T1. Design Homepage'.
        task_id = user_input.split(".")
        if reason_for_search == "Search":
            output_task(task_id[0])
        elif reason_for_search == "Edit":
            update_task_input(task_id[0])
    else:
        return False
    

def search_members():
    '''
    This function checks whether the user input the ID of the user they
    want to search for (for example: 'JSM') or the Name of the user they
    want to search for (for example: 'John Smith'), and runs the
    function to check if they exist depending on what is returned and
    outputs the search.
    '''
    user_searching = True
    # Prevents the program from returning to the homescreen when the
    # user types an invalid input.
    while user_searching == True:
        user_input = search_members_input()
        if user_input != None:
            member_exists = search_members_dictionary(user_input)
            # This if statement edits the user input depending on what 
            # the user input. If the user input the team member's name,
            # it would have to find the team member's ID aswell, but if 
            # the user just input the user's ID, it would just run the 
            # output function as it needs an ID.
            if member_exists == True:
                user_id = user_input.upper()
                output_user(user_id)
                user_searching = False
            elif type(member_exists) == str and len(member_exists) == 3:
                user_id = member_exists
                output_user(user_id)
                user_searching = False
            else:
                easygui.msgbox("Error: Member does not exist!")
        else:
            return



def search_members_dictionary(user_input):
    '''
    This function loops through the member dictionary, first checking if
    the user input an ID, and if it finds an ID it returns the ID to the
    function above this (search_members), and if it's not an ID it looks
    through the members dictionary for a name, and returns that name,
    to be output.
    '''
    for member_id in team_members:
        if member_id.lower() == user_input.lower():
            return True
        else:
            for member_value in team_members[member_id]:
                if member_value == "Name":
                    if team_members[member_id][member_value].lower() \
                    == user_input.lower():
                        return member_id


def search_members_input():
    '''
    This function creates an enterbox which creates a user-friendly way
    for the user to input what user they would like to search for,
    before passing that value onto other functions.
    '''
    box_title = "Task Manager - Search"
    box_msg = "Enter the team member's name or ID."
    user_input = easygui.enterbox(box_msg, box_title)
    validation = string_validation(user_input)
    if validation == True:
        return user_input
    else:
        return


#Functions for outputting.

def generate_report():
    '''
    This function creates a dictionary for every value in "Status
    Options" and automatically sets them to zero. It then loops through
    all the tasks, and if it finds a task with a set status, it
    increases the value of status by one.
    For example it sets "Not Started" to zero, until it finds a task
    with that status, and sets "Not Started" to 1.
    If it finds a status not found in the [status_options] list, it
    adds that new status to the dictionary and sets it to one, allowing
    more statuses to be added without it being hard-coded.
    '''
    status_counts = {}
    # Loops through all the pre-set status values and sets them to zero.
    for satus_values in status_options:
        status_counts[satus_values] = 0
    # Loops through all the tasks and finds their statuses.
    for task_id in task_list:
        status = task_list[task_id]['Status']
        if status in status_counts:
            status_counts[status] += 1
    output = [f"--- Total Project Progress Report: ---"]
    for key, value in status_counts.items():
        output.append(f"{key}: {value}")
    easygui.msgbox("\n".join(output), "Task Manager - Project Report")


def output_user(user_id):
    '''
    This function loops through a specific user's ID, grabbing all the
    information inside of it.
    It then outputs all of the values it found into a nice readable
    format.
    '''
    output = [f"--- {user_id}. {team_members[user_id]['Name']} ---"]
    for key, value in team_members[user_id].items():
        if key == 'Assigned Tasks':
            output.append("Assigned Tasks:")
            for assigned_task in value:
                output.append(f"- {assigned_task}." + 
                f" {task_list[assigned_task]['Title']}")
        else:
            output.append(f"{key}: {value}")
    easygui.msgbox("\n".join(output), title=team_members[user_id]["Name"])


def output_task(task_id):
    '''
    It loops through the task ID grabbing all its values, then outputs
    them in a nice, simple way.
    '''
    output = [f"--- {task_id}. {task_list[task_id]['Title']} ---"]
    for key, value in task_list[task_id].items():
        output.append(f"{key}: {value}")
    easygui.msgbox("\n".join(output), title=task_list[task_id]["Title"])

def output_all_tasks():
    '''
    It loops through the task_list dictionary then grabs all the
    information about each task, (title, description, priority,
    assignee, and status), then outputs them all in a nice readable
    format.
    '''
    output = []
    for task_id, task in task_list.items():
        output.append(f"--- {task_id}. {task['Title']} ---")
        for key, value in task.items():
            if key != "Title":
                output.append(f"{key}: {value}")
        output.append("")
    easygui.msgbox("\n".join(output), title="All Tasks")

#Functions used for updating/assigning Tasks.

def pre_update_task():
    '''
    This function allows the program to run an input through the search
    function, allowing it to specify that it is searching for a task to
    edit, and not a task to output, as there is no way to have the
    brackets with the menu, making this function necessary.
    '''
    search_tasks("Edit")
    return

def update_task_input(task_id):
    '''
    This function grabs the list provided to create a menu using those
    options, then outputs them all and checks what the user input then
    rerouts the user to a specific edit function based on the option
    that they chose.
    '''
    editable_fields = [field for field in task_tags]
    editable_fields.extend(extra_editable_task_tags)
    editable_fields.append("Cancel")
    box_msg = "Which Field would you like to edit?"
    box_title = "Task Manager - Edit Task"
    field_to_edit = easygui.buttonbox(box_msg, box_title, editable_fields)

    if field_to_edit == "Cancel" or field_to_edit == None:
        easygui.msgbox("No Field Selected. Edit Cancelled.")
        return
    
    updated_value = None
    # If the user were to select Priority to edit.
    if field_to_edit == "Priority":
        min_priority = 1
        max_priority = 3
        user_inputting_value = True
        # Prevents the user from returning to the homescreen when they
        # they an invalid input.
        while user_inputting_value == True:
            updated_value = input_value(field_to_edit)
            if updated_value == False:
                return
            validated_integer = integer_validation(updated_value,
                                                   min_priority, max_priority)
            if validated_integer != True:
                easygui.msgbox(validated_integer, "Error")
            else:
                user_inputting_value = False
    # If the user were to select the Status to edit.
    elif field_to_edit == "Status":
        updated_value = update_status(task_id)
        if updated_value == False:
            return
    # If the user were to select the Assignee to edit.
    elif field_to_edit == "Assignee":
        updated_value = assign_task_selector(task_id)
        if updated_value == False:
            return
        output_task(task_id)
    # If the user were to select the Title or the Description to edit.
    else:
        user_input = input_value(field_to_edit)
        if user_input == False:
            return
        updated_value = user_input
    if updated_value != None:
        update_task(updated_value, task_id, field_to_edit)

        
def update_task(updated_value, task_id, field_to_edit):
    '''
    This function is used to actually change the value in the
    dictionary, then output a success message, the edit comes from the
    update_task_input() function.
    '''
    if updated_value != None:
        task_list[task_id][field_to_edit] = updated_value
        easygui.msgbox(f"{field_to_edit} updated sucessfully.", 
                       "Edit Complete")
        output_task(task_id)

def update_status(task_id):
    '''
    This function creates a menu of buttons which allow the user to
    change the status of the selected task. The list of editable tasks
    is able to be changed in the list at the top. This function then
    returns the user input to the main edit_task_input() function.
    '''
    box_msg = (f"What would you like to set the status of " + 
    f"{task_id}: {task_list[task_id]['Title']} to?")
    box_title = "Task Manager - Editing Status"
    # Sets the options the user can choose to the list defined near the
    # top of the program.
    options = status_options
    options.append("Cancel")
    user_input = easygui.buttonbox(box_msg, box_title, options)
    if user_input == "Cancel" or user_input == None:
        easygui.msgbox("Edit cancelled. Returning")
        options.remove("Cancel")
        return False
    else:
        if user_input == "Complete":
            unassign_task(task_id)
        # This is done to prevent the 'Done' option showing up multiple
        # times when the user goes through the update function multple
        # times.
        options.remove("Cancel")
        return user_input

def input_value(field_to_edit):
    '''
    As this is the only place where user's input a single value, it is
    used for the edit function. It can be used to update the title or
    description. It calls the validation function to ensure that the
    text was input and if it was, returns the text to the main
    edit_task_input() function.
    '''
    box_title = "Editing Task"
    box_msg = f"Enter what you would like to change {field_to_edit} to?"
    user_input = easygui.enterbox(box_msg, box_title)
    if user_input == None or user_input == "Cancel" or len(user_input) == 0:
        box_msg = "Edit Cancelled"
        box_title = "Task Manager - Updating Value"
        easygui.msgbox(box_msg, box_title)
        return False
    else:
        return user_input

def assign_task_selector(task_id):
    '''
    This creates a menu out of all the users, in a choicebox, and
    allows the user to select one. The selected user then goes to an
    assign or un-assign function, with the selected task. It prevents
    the task from being assigned if its status is set to complete.
    '''
    box_msg = (f"What member would you like to assign:" +
    f"\n{task_id}. {task_list[task_id]['Title']}\n")
    box_title = "Task Manager - Assigning a Task"
    choices = ["None (Un-assign Task)"]
    for member_id in team_members:
        for key in team_members[member_id]:
            if key == "Name":
                choices.append(f"{member_id}. " +
                               f"{team_members[member_id]['Name']}")
    choice = easygui.choicebox(box_msg, box_title, choices)
    if task_list[task_id]['Status'] != "Complete":
        if choice == "None (Un-assign Task)":
                unassign_task(task_id)
                return
        elif choice != None:
                user_id = choice.split(".")
                user_id = user_id[0]
                unassign_task(task_id)
                assign_task(task_id, user_id)
                return user_id
        else:
            box_msg = "You cancelled selection. Returning to home screen."
            box_title = "Task Manager - Error"
            easygui.msgbox(box_msg, box_title)
            return False
    else:
        box_msg = ("Error: The task is already complete! " +  
        "Please change the task status to assign this task to a user.")
        box_title = "Task Manager - Error"
        easygui.msgbox(box_msg, box_title)
        return False


def unassign_task(task_id):
    '''
    Checks if the task has anybody assigned to it, and if it does then
    it removes assigned user, then removes the task from their task
    list.
    If the task has nobody assigned to it, it is already un-assigned
    and thus just returns to the previous function.
    Return True: is done if the task already has nobody assigned to it.
    '''
    member_id = task_list[task_id]['Assignee']
    if member_id == "None" or member_id == None:
        return True
    else:
        for assigned_tasks in team_members[member_id]['Assigned Tasks']:
            if assigned_tasks == task_id:
                team_members[member_id]['Assigned Tasks'].remove(task_id)
        task_list[task_id]["Assignee"] = "None"
    return member_id


def assign_task(task_id, user_id):
    '''
    This function assigns a specified member to a specific task, and
    updates both the task_list dictionary and team_members dictionary.
    It changes the assignee of the task_list dictionary to the selected
    user, and changes the team_members dictionary by adding the task
    to their task list.
    '''
    team_members[user_id]['Assigned Tasks'].append(task_id)
    task_list[task_id]['Assignee'] = user_id
    box_title = "Task Manager - Success"
    box_msg = (f"Sucessfully assigned Task {task_list[task_id]['Title']}"  +
    f" to user {team_members[user_id]['Name']}!")
    easygui.msgbox(box_msg, box_title)
    return

#Functions used for adding Tasks.

def generate_task_id():
    '''
    Grabs the number of tasks and increases it by one, to create a new
    unique ID.
    '''
    number_of_tasks = len(task_list) + 1
    task_id = f"T{number_of_tasks}"
    return task_id

def input_multiple_values(values_to_enter, title):
    '''
    Creates a multi-enter box and sends the values that the user
    inputs to be validated, and check if there is any missing
    information, if not, the function returns to the home page.
    '''
    box_msg = f"Please input the info to {title}"
    box_title = title
    user_inputting_values = True
    # Prevents the user from returning to the homescreen when they type
    # an invalid input, and just re-opens the multi enter box.
    while user_inputting_values == True:
        user_input = easygui.multenterbox(box_msg,box_title,values_to_enter)
        if user_input != None:
            checked_values = string_validation(user_input)
            if checked_values == True:
                min_priority = 1
                max_priority = 3
                validated_integer = integer_validation(user_input[2], 
                                            min_priority, max_priority)
                if validated_integer != True:
                    easygui.msgbox(f"{validated_integer}", "Error")
                else:
                    user_inputting_values = False
                    return user_input
        else:
            return


                    

def create_new_task():
    '''
    Guides the user through the task creation process, by asking for the
    Title, Description, and Priority, then validates those values, then
    generates a unique task ID, then allows the user to assign the task
    to a team member.
    If anything if invalid or cancelled, it returns to the main menu.
    '''
    title = "Task Manager - Create a New Task"
    user_input = input_multiple_values(task_tags, title)
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
        task_id = generate_task_id()
        task_list[task_id] = new_task
        assignne_selection = assign_task_selector(task_id)
        if assignne_selection == False:
            task_list.pop(task_id)
            return
        else:
            output_task(task_id)


def user_menu():
    '''
    Displays the main menu of the Task Manager Program. It allows the
    user to choose from a list of items, and is running on a loop so
    that if nothing else if being shown, the main menu will show, which
    prevents the program from randomly closing.
    '''
    options = {
        "Add a New Task": create_new_task,
        "Update a Task": pre_update_task,
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
        # This loop loops through the options dictionary that was 
        # defined above and adds the title of the title to a button in 
        # the button box. Then, when an option is selected, it runs the 
        # function (key) ascociated with the title.
        for action in options:
            choices.append(action)
        
        selection = easygui.buttonbox(box_msg,box_title,choices)
        if selection is None:
            selection = "Exit"
        get_input = options[selection]()
        
user_menu()