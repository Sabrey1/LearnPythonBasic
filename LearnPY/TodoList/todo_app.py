from datetime import datetime

#1.create folder and file structure

#2. create class
class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"

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
                print(f"Task {task_id} completed successfully!")
                return
        print(f"Task with id {task_id} not found.")

if __name__ == "__main__":
    todo = TodoList()
    todo.add_task("Build todo list app")
    todo.add_task("Read Book About python")
    todo.view_task()
    todo.complete_task(task_id= 1)
    todo.complete_task(task_id= 2)
    todo.view_task()
