"""
Author      : Vishal Panchal
Created At  : 9 August 2019
Description : This is sample flask application with sample API to create to do list.
"""

from flask import Flask, request, jsonify, render_template,redirect
from controller import TaskController
import os

app = Flask(__name__)
app.config["DEBUG"] = True

# route to save task
@app.route('/saveTask', methods=['POST','GET'])
def save_task():
    task_Object = {}
    if request.method == "POST":
        task_Object["task"] = request.form['taskName']
        task_Object["date"] = request.form['dateName']
        task_Object["status"] = request.form['statusName']
        save_Task_Result = TaskController.addTask(task_Object)
    return redirect("../viewTask")

# route to landing page 
@app.route('/')
def add_task():
    return render_template('AddTask.html')

# route to view task page
@app.route('/viewTask')
def view_task():
    view_Task = TaskController.viewTask()
    return render_template('ViewTask.html', length = len(view_Task) ,ToDoList = view_Task)

if __name__ == "__main__":
    app.run()