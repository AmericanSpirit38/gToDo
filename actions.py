import JSON_manager
import os

class GTodo:
    def __init__(self, file_path="data.json"):
        self.JSon_manager = JSON_manager.JSONManager(file_path)
        self.tasks = self.JSon_manager.read_json() or []
        print("GTodo initialized. Tasks loaded.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks found. Check your data.json file.")
            return
        for idx, task in enumerate(self.tasks, start=1):
            status = "✓" if task.get("completed") else "✗"
            print(f"{idx}. [{status}] {task.get('title')} - {task.get('description')}")
    def add_task(self, title, description, priority, due_date):
        id = len(self.tasks) + 1
        new_task = {
                "id": id,
                "title": title,
                "description": description,
                "priority": priority,
                "due_date": due_date,
                "completed": False
        }
        self.JSon_manager.append_json(new_task)
        self.tasks.append(new_task)
        print("Task added successfully.")
    def remove_task(self, task_id):
        self.JSon_manager.remove_json(task_id)
        self.tasks = self.JSon_manager.read_json()
        print("Task removed successfully.")
    def mark_task_completed(self, task_id):
        self.JSon_manager.edit_json(task_id,"completed", True)




if __name__ == "__main__":
    gtodo = GTodo()