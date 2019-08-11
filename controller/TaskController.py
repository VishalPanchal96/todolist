"""
Author      : Vishal Panchal
Created At  : 9 August 2019
Description : This is a controller file for adding new task and viewing added tasks
"""

from model import Task
import os
import json


# Function viewTasK(): to view all the added tasks
# Argument: Nothing
# Created By: Vishal Panchal (10/08/2019)
def viewTask():
    try:
        return Task.Task.read_todolist_data()
    except:
        return 'Unable to fetch tasks'

   
# Function addTask(): to add a new task
# Argument: task object
# Created By: Vishal Panchal (10/08/2019)    
def addTask(task):
    try:
        get_All_Task = Task.Task.read_todolist_data()
        get_All_Task.append(json.loads(json.dumps(task)))
        Task.Task.write_json_data(get_All_Task)
        return 'Record Added'
    except:
        return 'Unable to add new task'