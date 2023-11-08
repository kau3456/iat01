import json

class Task:
    def __init__(self, title, description, status="Incomplete"):
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        print("Title : ",self.title,",  Description : ",self.description,",  Status : ",self.status)
        
class ToDoList:
    def __init__(self):
        self.tasks = []
        
    def add_task(self, title, description):
        new_task = Task(title, description)
        self.tasks.append(new_task)
        print("Task ",title,"added to the To-Do List.")

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print("Task ",title,"deleted from the To-Do List.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the To-Do List.")
        else:
            for task in self.tasks:
                print(task)

    def save_tasks(self, file_name):
        with open(file_name, 'w') as file:
            task_list = [task.__dict__ for task in self.tasks]
            json.dump(task_list, file)
        print("To-Do List saved to ",file_name)

    def load_tasks(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                self.tasks = [Task(task['Title'], task['Description'], task['Status']) for task in data]
            print("To-Do List loaded from ",file_name)
        except FileNotFoundError:
            print("File ",file_name,"not found. No tasks loaded.")

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks to File")
        print("5. Load Tasks from File")
        print("6. Quit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == '2':
            title = input("Enter task title to delete: ")
            todo_list.delete_task(title)
        elif choice == '3':
            todo_list.view_tasks()
        elif choice == '4':
            file_name = input("Enter the file name to save tasks: ")
            todo_list.save_tasks(file_name)
        elif choice == '5':
            file_name = input("Enter the file name to load tasks from: ")
            todo_list.load_tasks(file_name)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

