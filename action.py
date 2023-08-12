from tasklist import *
import datetime
import pickle

class Action:

    def __init__(self, action: str):
        self.action = action

    @staticmethod
    def action_responding(tasklists: list):
        action = input("Make a decision: ")

        if action == "Make new tasklist":
            new_list = TaskList(input("Enter your tasklist name: "))
            tasklists.append(new_list)

        elif action == "Check your lists":
            if not tasklists:
                print("Your Task Manager is empty.")

            for index, tasklist in enumerate(tasklists):
                print(f"{index + 1}.{tasklist.tasklist_name}")

            view_action = True if input("Would you like to view a tasklist?: Y/N:\n").lower() == "y" else False
            if view_action:
                view_task = int(input("Enter the number of the tasklist you would like to see: ")) - 1
                if view_task > len(tasklists) - 1:
                    print("Sorry this tasklist does not exist!")
                print(tasklists[view_task])
        elif action == "Add to list":
            add_task = int(input("Enter the number of the tasklist you would like to add: ")) - 1
            if add_task > len(tasklists) - 1:
                print("Sorry this tasklist does not exist!")
            new_task = Task(
                task_name=input("Please enter task-name: "),
                deadline=input("Enter deadline dd-hh-mm: "),
                date=datetime.datetime.now().date(),
                note=input("Enter note: ")
            )
            tasklists[add_task].add_task(new_task)

        elif action == "Delete task":
            delete_task = int(input("Enter the number of the tasklist you would like to delete: ")) - 1
            if delete_task > len(tasklists) - 1:
                print("Sorry this tasklist does not exist!")
            tasklists[delete_task].delete_task()

        elif action == "Save task lists":
            if not tasklists:
                print("Tasklist is empty!")
            with open(input("Enter name for your task lists: ") + ".tl", 'wb') as handle:
                pickle.dump(tasklists, handle, protocol=pickle.HIGHEST_PROTOCOL)
                print("Saved")

        elif action == "Load previous task lists!":
            with open(input("Enter previous task lists: ") + '.tl', 'rb') as handle:
                tasklists = pickle.load(handle)
                print(tasklists)
        return tasklists

