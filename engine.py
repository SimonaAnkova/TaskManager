import action


def run():
    print("Make new tasklist\n"
          "Check your lists\n"
          "Add to list\n"
          "Delete task\n"
          "Save task lists\n"
          "Load previous task lists!\n")
    tasklists = []
    while True:
        tasklists = action.Action.action_responding(tasklists)