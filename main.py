def main_menu():
    print("==== Smart Study Planner ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Exit")

    choice = input("Please enter your choice (1-6): ")
    return choice

tasks = []

while True:
    choice = main_menu()
    if choice == '1':
        task = input("Enter the task description: ")
        if task=="":
            print("Task description cannot be empty.")
            continue
        else:
            tasks.append({"Name": task, "Status": "Pending"})
            print(f"Task '{task}' added.")
    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task['Name']} - {task['Status']}")
    elif choice == '6':
        print("Exiting the Smart Study Planner. Goodbye!")
        break
    else:
        continue
