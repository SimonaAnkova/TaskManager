import tkinter as tk
from tkinter import messagebox
from action import *

window = tk.Tk()
window.geometry("700x400")

def display_weather():
    city = user_input.get()
    output = API_Manager.get_current_weather(city)
    output_label.config(text=output)


button = tk.Button(
    text="Make new task list",
    width=20,
    height=2,
    bg="red",
    fg="white",
    command = display_weather
)
button.pack()

button = tk.Button(
    text="Check your list",
    width=20,
    height=2,
    bg="red",
    fg="white",
    #command = Action.tasklists.append(new_list)
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