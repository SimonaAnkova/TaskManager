class TaskList:
    def __init__(self, tasklist_name):
        self.tasklist_name = tasklist_name
        self.lst = []

    def get_name(self):
        return self.tasklist_name

    def add_task(self, *task):
        self.lst.extend(task)

    def delete_task(self, *task):
        self.lst.remove(task)

    def get_tasks(self):
        _str = f"{self.tasklist_name}:\n"
        for index, task in enumerate(self.lst):
            _str += f"{index + 1}. {task}\n"
        return _str

    def __str__(self):
        return self.get_tasks()


class Task:
    def __init__(self, task_name):
        self.task_name = task_name


    def __str__(self):
        return f"Task name: {self.task_name}"








