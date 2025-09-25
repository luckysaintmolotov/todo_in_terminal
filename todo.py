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
    "skip_or_reschedule":bool() 
    
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
