import json

class JSONManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_json(self):
        """Reads JSON data from the file and returns it as a Python object."""
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
            return None
        except json.JSONDecodeError:
            print(f"Error: The file {self.file_path} is not valid JSON.")
            return None
    def append_json(self, new_data):
        """Appends new data to the existing JSON file."""
        data = self.read_json() or []
        data.append(new_data)
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    def remove_json(self, task_id):
        """Removes a task by its ID from the JSON file."""
        data = self.read_json() or []
        data = [task for task in data if task.get("id") != task_id]
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    def edit_json(self, task_id, category, new_data):
        """Edits an existing task in the JSON file."""
        to_edit = None
        data = self.read_json() or []
        for idx, task in enumerate(data):
            if task.get("id") == task_id:
                to_edit = data[idx]
                break
        if to_edit:
            to_edit[category] = new_data
            self.remove_json(task_id)
            self.append_json(to_edit)
        else:
            print(f"Error: Task with ID {task_id} not found.")
            return