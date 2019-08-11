"""
Author      : Vishal Panchal
Created At  : 9 August 2019
Description : This is a model file for adding and reading tasks from data 
"""


import json
import os

#Path constant to taskList json file
PATH_TO_TASKLIST_JSON = "../data/taskList.json"

class Task:
    def read_todolist_data():
        fp = open(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_TASKLIST_JSON), encoding="utf8")
        data = json.loads(fp.read())
        return data

    def write_json_data(data_source):
        with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), PATH_TO_TASKLIST_JSON), 'w') as json_file:
            json.dump(data_source, json_file)
        return