import actions
from tabulate import tabulate
import shlex
from colorama import init, Fore, Style

class GTodo:
    def __init__(self):
        self.actions = actions.Actions("data.json")

init(autoreset=True)

gtodo = GTodo()
command_list = ["list", "add", "remove","edit", "exit", "help"]
print(Fore.LIGHTBLUE_EX + "Welcome to GTodo!" + Style.RESET_ALL)
print(Fore.LIGHTWHITE_EX + "Available commands: list, add, remove, edit, exit" + Style.RESET_ALL)
print(Fore.RED + "WARNING: " + Style.RESET_ALL + Fore.LIGHTWHITE_EX + "If you enter an input with spaces (e.g., a task title or description), please enclose it in quotes.(e.g. if your task title is Buy groceries, enter it as \"Buy groceries\")" + Style.RESET_ALL)
while True:
    inp = shlex.split(input("GTodo> "))
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
                print(tabulate(rows, headers=headers, tablefmt="github"))
            except Exception:
                print(df.to_string(index=False))
        if command == "add":
            title, description, priority, due_date= inp[1], inp[2], inp[3], inp[4]
            if not title or not description or not priority or not due_date:
                print("Error: Missing required fields. Usage: add <title> <description> <priority> <due_date>")
                continue
            gtodo.actions.add_task(title, description, priority, due_date)
        if command == "exit":
            print("Exiting GTodo. Goodbye!")
            break

