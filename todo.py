import pandas as pd
from datetime import datetime

"""
# What it should contain

- Name of the thing
- When the thing needs to be done by
- Does the thing have a duration
- Importance of the thing
- Reschedule or Skip said thing
- Save to local
# Variables

name_of_task : string
task_creation_date : date time
task_duration  : int
task_completion_date : date time
importance_of_task : list
skip_or_reschedule : bool


# What it should be capable of doing

- Get the name of the thing from user
    - This should also sanitize the input
    - Validate the input
    - And check for duplicates
        -If yes then it must be renamed
- Get the duration of the thing 
    - This should validate and sanitize the input
- Automatically timestamp the creation of the thing
- Ask for the completion date by input
    - This too should be validated and cleansed 
- Ask the user to set the importance of the task
- Check if thing needs to be skipped or rescheduled
- Ask to save the list of things 
- Ask to load list/s of things


# The Future Features

- Web interface

"""


TODO = {
    "name":"",
    "creation_date":"",
    "completion_date":"",
    "task_duration":"",
    "priority":"",
    "status":bool(),
    "skip_or_reschedule":bool(), 
    "reschedule_date":""
}

def get_name_of_task():
    while True:
        task_name = input("Name of the task:\n").lower().strip()
        if task_name:
            break
        print("Please enter a valid task name.")

    response = input(f"Is - {task_name} - correct? Y/n:\n").lower().strip()
    while True:
        if response not in ['yes', 'y', 'no', 'n']:
            print("Invalid input. Please enter 'yes', 'y', 'no', or 'n'.")
            response = input("Try again: ").lower().strip()
        else:
            break

    if response in ['yes', 'y']:
        return task_name
    else:
        print("Task name not confirmed. Returning original value.")
        return task_name
    
def set_creation_date_to_today():
    current_datetime = datetime.today()
    return datetime.strftime(current_datetime,"%Y-%m-%d %H:%M")
    
def get_completion_date_and_time():
    while True:
        completion_date_time = input("Date and Time to finish task (YYYY-MM-DD HH:MM): ").strip()
        try:
            return datetime.strptime(completion_date_time, "%Y-%m-%d %H:%M")
        except ValueError:
            print(f"Invalid date and time format: {completion_date_time}")

def set_duration():
    duration = input("duration of task(HH:MM):\n")
    
    try:
        duration = datetime.strptime(duration, "%H:%M")
        if duration.hour <= 23 and duration.minute <=59:
            duration = {
                "hour":duration.hour,
                "minute":duration.minute
                }
            return duration
        else:
            print(f"Invalid input - {duration}")
    except ValueError:
        print(f"Invalid format -{duration}- it is not valid time")

def set_priority():
    priority = ('no','low','medium','high','IMPORTANT')
    while True:
        selection = input(f"""
Please select from the following
1: {priority[0]}
2: {priority[1]}
3: {priority[2]}
4: {priority[3]}
5: {priority[4]}
""")
        if int(selection.isdigit()):
            selection = int(selection)
            try:
                    return priority[selection-1]
            except IndexError:
                    print(f"{selection} is not a valid selection")
            
        else:
            print(f"{selection} is not a valid integer")
        
def skip_or_reschedule():
    while True:
        user_input = input("(R)eschedule or (S)kip? r/s:\n")
        
        if user_input in ['r','s','reschedule','skip']:
            if user_input in ['r','reschedule']:
                skip_or_reschedule={False,True}
                rescheduled_date = get_completion_date_and_time()
                return skip_or_reschedule,rescheduled_date
            else:
                return True,False,None
        else:
            print(f"Incorrect input {user_input}")

print(skip_or_reschedule())