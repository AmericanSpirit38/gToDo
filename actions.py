import JSON_manager
import pandas as pd
import os

class Actions:
    def __init__(self, file_path="data.json"):
        self.JSon_manager = JSON_manager.JSONManager(file_path)
        self.tasks = self.JSon_manager.read_json() or []

    def list_tasks(self, parse_dates=True, date_col='due_date', set_index='id'):
        """
        Print tasks (default) or return a pandas DataFrame when as_dataframe=True.
        - parse_dates: if True, attempts to parse `date_col` to datetime
        - date_col: name of date field in tasks
        - set_index: column to set as index (use None to keep default)
        """
        self.tasks = self.JSon_manager.read_json() or []
        if not self.tasks:
            print("No tasks found. Check your data.json file.")
            return

        return self.tasks_to_dataframe(parse_dates=parse_dates, date_col=date_col, set_index=set_index)

    def tasks_to_dataframe(self, parse_dates=False, date_col='due_date', set_index='id'):
        """
        Return tasks as a pandas DataFrame.
        - parse_dates: if True, attempts to parse `date_col` to datetime
        - date_col: name of date field in tasks
        - set_index: column to set as index (use None to keep default)
        """
        self.tasks = self.JSon_manager.read_json() or []
        if not self.tasks:
            return pd.DataFrame()
        df = pd.DataFrame(self.tasks)
        if 'completed' in df.columns:
            df['completed'] = df['completed'].astype(bool)
        if parse_dates and date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
        if set_index and set_index in df.columns:
            df = df.set_index(set_index)
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
