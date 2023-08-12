import tkinter as tk
from tkinter import messagebox
from action import *
from tasklist import *
from functools import partial

window = tk.Tk()
window.geometry("700x400")

tasklists = []

def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    newWindow = tk.Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    tk.Label(newWindow,
             text="Enter Tasklists").pack()

    tasklist_name = tk.StringVar()
    tasklist = tk.Entry(newWindow, width=35, textvariable=tasklist_name).pack()

    def create_tasklist():
        name = tasklist_name.get()
        global tasklists
        tasklists.append(TaskList(name))
        messagebox.showinfo("Success!", f"Created  {name}")


    button = tk.Button(newWindow,
        text="Create your list",
        width=20,
        height=2,
        bg="red",
        fg="white",
        command = create_tasklist
    )
    button.pack()




button = tk.Button(
    text="Make new task list",
    width=20,
    height=2,
    bg="red",
    fg="white",
   command = openNewWindow
)
button.pack()

def check_tasklists():
    global tasklists
    tasklists_str = ", ".join([tl.get_name() for tl in tasklists])
    messagebox.showinfo("Tasklists",tasklists_str)

def check_tasklists_buttons():
    global tasklists
    newWindow = tk.Toplevel(window)

    # sets the title of the
    # Toplevel widget
    newWindow.title("Tasklists")

    def edit_tasklist(tl):
        taskwindow = tk.Toplevel(newWindow)

        # sets the title of the
        # Toplevel widget
        taskwindow.title(tl.get_name())

        tk.Label(taskwindow,
                 text="Tasks").pack()

        tk.Label(taskwindow,
                 text=str(tl)).pack()

        tk.Label(taskwindow,
                 text="Add Task").pack()

        task_name = tk.StringVar()
        task_name_f = tk.Entry(taskwindow, width=35, textvariable=task_name).pack()

        indx = tasklists.index(tl)

        def add_task():
            tn = task_name.get()
            tl.add_task(Task(tn))
            tasklists[indx] = tl

        button = tk.Button(taskwindow,
                           text="task name",
                           width=20,
                           height=2,
                           bg="red",
                           fg="white",
                           command=add_task
                           )
        button.pack()

    for tl in tasklists:
        tk.Button(newWindow,
                  text=tl.get_name(),
                  width=20,
                  height=2,
                  bg="red",
                  fg="white",
                  command=partial(edit_tasklist, tl)
                  ).pack()

button = tk.Button(
    text="Check your lists",
    width=20,
    height=2,
    bg="red",
    fg="white",
    command = check_tasklists_buttons
)
button.pack()

button = tk.Button(
    text="Add to list",
    width=20,
    height=2,
    bg="red",
    fg="white",
    #command = Action.tasklists.append(new_list)
)
button.pack()

button = tk.Button(
    text="Delete task",
    width=20,
    height=2,
    bg="red",
    fg="white",
    #command = Action.tasklists.append(new_list)
)
button.pack()

button = tk.Button(
    text="Save task lists",
    width=20,
    height=2,
    bg="red",
    fg="white",
    #command = Action.tasklists.append(new_list)
)
button.pack()

button = tk.Button(
    text="Load previous task lists!",
    width=20,
    height=2,
    bg="red",
    fg="white",
    #command = Action.tasklists.append(new_list)
)
button.pack()

window.mainloop()