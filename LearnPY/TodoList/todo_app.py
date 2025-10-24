from datetime import datetime
import json

#1.create folder and file structure

#2. create class
class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

#3. create methods
    def add_task(self, description):
        """Add a new task MORE INFO"""
        task = {
            "id": len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{description}' add successfully!")

#4. Viewing Tasks
    def view_task(self):
        """View tasks"""
        if not self.tasks:
            print("No tasks found.")
            return
        print("\nYour ToDo List:")
        print("-" * 50)
        for task in self.tasks:
            
            status = "Completed" if task['completed'] else "Not Completed"
            #1. [] Build todo list app
            #2. [] Read Book About python
            print(f"{task['id']}. [{status}] { task['description']}")
        print("-" * 50)

#5. Complite Task
    def complete_task(self, task_id):
        """Complete a task"""
        #1. Loop through tasks property
        #2. check for task_id
        #3. mark task as completed
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task {task_id} completed successfully!")
                return
        print(f"Task with id {task_id} not found.")

#6. delete task
    def delete_task(self, task_id):
        """Delete a task"""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task {task_id} deleted successfully!")
                return
        print(f"Task with id {task_id} not found.")

#7. save file  

    def save_tasks(self):
        """Save tasks to file"""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent = 2 )

    def load_tasks(self):
        """Load tasks from file"""
        try:
            with open(self.filename, "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []
    
#create menu
def main():
    todo = TodoList()
    while True:
        print("\n +++ TODO List App +++")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if(choice == '1'):
            description = input("Enter task descrpition:")
            todo.add_task(description=description)
        elif(choice == '2'):
            todo.view_task()
        elif(choice == '3'):
            todo.view_task()
            try:
                task_id = int(input("Enter task id: "))
                todo.complete_task(task_id=task_id)
            except ValueError:
                print("Invalid task id. Please try again.")
        elif(choice == '4'):
            todo.view_task()
            try:
                task_id = int(input("Enter task id: "))
                todo.delete_task(task_id = task_id)
            except ValueError:
                print("Invalid task id. Please try again.")
        
        elif(choice == '5'):
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todo = TodoList()
    main()
