import actions
from tabulate import tabulate
import shlex
from colorama import init, Fore, Style
import os

class GTodo:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_path = os.path.join(base_dir, "data.json")
        self.actions = actions.Actions(data_path)

init(autoreset=True)

gtodo = GTodo()
command_list = ["list", "add", "remove","edit", "exit", "help"]
print(Fore.CYAN + "Welcome to GTodo!" + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX + "Available commands: list, add, remove, edit, exit" + Style.RESET_ALL)
print(Fore.RED + "WARNING: " + Style.RESET_ALL + Fore.LIGHTWHITE_EX + "If you enter an input with spaces (e.g., a task title or description), please enclose it in quotes.(e.g. if your task title is Buy groceries, enter it as \"Buy groceries\")" + Style.RESET_ALL)
while True:
    inp = shlex.split(input(Fore.LIGHTWHITE_EX+ "GTodo> " + Style.RESET_ALL + Fore.GREEN))
    if not inp:
        continue
    command = inp[0].lower()
    if command in command_list:
        if command == "list":
            # request a pandas DataFrame from actions
            df = gtodo.actions.list_tasks(parse_dates=False, set_index=None)
            if df is None:
                continue
            # empty DataFrame message
            try:
                empty = df.empty
            except Exception:
                empty = False
            if empty:
                print("No tasks found.")
                continue
            # pretty print: prefer tabulate, fallback to pandas' to_string
            try:
                # use reset_index so index column (like id) is shown as a column
                rows = df.reset_index().values.tolist()
                headers = list(df.reset_index().columns)
                colored_headers = [Fore.CYAN + str(h) + Style.RESET_ALL + Fore.LIGHTWHITE_EX for h in headers]
                print(Fore.WHITE + tabulate(rows, headers=colored_headers, tablefmt="github") + Style.RESET_ALL)
            except Exception:
                print(df.to_string(index=False))
        elif command == "add":
            title, description, priority, due_date= inp[1], inp[2], inp[3], inp[4]
            if not title or not description or not priority or not due_date:
                print(Fore.RED + "Error: " + Fore.LIGHTWHITE_EX +"Missing required fields. Usage: add <title> <description> <priority> <due_date>" + Style.RESET_ALL)
                continue
            gtodo.actions.add_task(title, description, priority, due_date)
            print(Fore.LIGHTWHITE_EX + "Task added successfully." + Style.RESET_ALL)
        elif command == "remove":
            try:
                task_id = int(inp[1])
            except (IndexError, ValueError):
                print(Fore.RED + "Error: " + Fore.LIGHTWHITE_EX +"Please provide a valid task ID to remove. Usage: remove <task_id>" + Style.RESET_ALL)
                continue
            gtodo.actions.remove_task(task_id)
            print(Fore.LIGHTWHITE_EX + f"Task {task_id} removed successfully." + Style.RESET_ALL)
        elif command == "edit":
            try:
                task_id = int(inp[1])
                category = inp[2]
                new_data = " ".join(inp[3:])
            except (IndexError, ValueError):
                print(Fore.RED + "Error: " + Fore.LIGHTWHITE_EX +"Please provide valid inputs to edit. Usage: edit <task_id> <category> <new_data>" + Style.RESET_ALL)
                continue
            gtodo.actions.edit_task(task_id, category, new_data)
            print(Fore.LIGHTWHITE_EX + f"Task {task_id} updated successfully." + Style.RESET_ALL)
        elif command == "exit":
            print(Fore.LIGHTWHITE_EX + "Exiting GTodo. Goodbye!" + Style.RESET_ALL)
            break
        elif command == "help":
            print(Fore.CYAN + "Available commands:" + Style.RESET_ALL)
            print(Fore.LIGHTWHITE_EX + "Use help <command> for more information" + Style.RESET_ALL)
            print(Fore.CYAN + "    list" + Fore.LIGHTWHITE_EX + " - Display tasks" + Style.RESET_ALL)
            print(Fore.CYAN + "    add" + Fore.LIGHTWHITE_EX + " - Add a new task" + Style.RESET_ALL)
            print(Fore.CYAN + "    remove" + Fore.LIGHTWHITE_EX + " - Remove a task" + Style.RESET_ALL)
            print(Fore.CYAN + "    edit" + Fore.LIGHTWHITE_EX + " - Edit a task" + Style.RESET_ALL)
            print(Fore.CYAN + "    exit" + Fore.LIGHTWHITE_EX + " - Exit the application" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Error: " + Fore.LIGHTWHITE_EX + f"Unknown command '{command}'. Type 'help' for a list of commands." + Style.RESET_ALL)


