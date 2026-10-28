tasks = []

while True:
    action = int(input("What do you want to do? \n 1. Add task \n 2. Show tasks"
                       " \n 3. Delete task \n 4. Exit \n Choose an option: "))
    if action == 1:
        task = input("Please enter your task: ")
        if not task.strip():
            print("Please enter a valid task!")
        else:
            tasks.append(task)
            print("Your task has been added!")
    elif action == 2:
        if len(tasks) == 0:
            print("No tasks added!")
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
            number = int(input())
            if 1 <= number <= len(tasks):
                index = number - 1
                tasks.pop(index)
                print("Your task has been deleted!")
            else:
                print("Invalid number")
    elif action == 4:
        print("Goodbye!")
        break
    else:
        print("Please enter a valid option!")