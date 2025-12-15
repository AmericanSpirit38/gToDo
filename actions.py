import JSON_manager
import pandas as pd
import os

class Actions:
    def __init__(self, file_path="data.json"):
        self.JSon_manager = JSON_manager.JSONManager(file_path)
        self.tasks = self.JSon_manager.read_json() or []

    def list_tasks(self, completed, all_tasks):
        self.tasks = self.JSon_manager.read_json() or []
        if not self.tasks:
            return pd.DataFrame()
        if not all_tasks:
            self.tasks = [task for task in self.tasks if task.get("completed") == completed]

        return self.tasks_to_dataframe()

    def tasks_to_dataframe(self):
        """
        Return tasks as a pandas DataFrame.
        - parse_dates: if True, attempts to parse `date_col` to datetime
        - date_col: name of date field in tasks
        - set_index: column to set as index (use None to keep default)
        """
        if not self.tasks:
            return pd.DataFrame()
        df = pd.DataFrame(self.tasks)
        return df
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
    def remove_task(self, task_id):
        self.JSon_manager.remove_json(task_id)
        self.tasks = self.JSon_manager.read_json()
    def mark_task_completed(self, task_id):
        self.JSon_manager.edit_json(task_id,"completed", True)
    def edit_task(self, task_id, category, new_data):
        self.JSon_manager.edit_json(task_id, category, new_data)
    def search_tasks(self, keyword):
        self.tasks = self.JSon_manager.read_json() or []
        filtered_tasks = [task for task in self.tasks if keyword.lower() in task.get("title", "").lower() or keyword.lower() in task.get("description", "").lower()]
        self.tasks = filtered_tasks
        return self.tasks_to_dataframe()
