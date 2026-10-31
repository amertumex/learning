import json
from pathlib import Path

PATH = Path(__file__).parent /"todo.json"

def load():
    if not PATH.exists():
        return []
    with open(PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save(tasks):
    with open(PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

tasks = load()

while True:
    try:
        action = int(input("What do you want to do? \n 1. Add task \n 2. Show tasks"
                           " \n 3. Delete task \n 4. Exit \n Choose an option: "))
    except ValueError:
        print("Please enter a number")
        continue

    if action == 1:
        task = input("Please enter your task: ")
        if not task.strip():
            print("Please enter a valid task")
        else:
            tasks.append(task)
            save(tasks)
            print("Your task has been added")
    elif action == 2:
        if len(tasks) == 0:
            print("No tasks added")
        else:
            print("Tasks: ")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
    elif action == 3:
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            print("Choose task for delete: ")
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")
            try:
                number = int(input())
            except ValueError:
                print("Invalid number")
                continue
            if 1 <= number <= len(tasks):
                index = number - 1
                tasks.pop(index)
                save(tasks)
                print("Your task has been deleted")
            else:
                print("Invalid number")
    elif action == 4:
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option")