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
    elif choice == '3':
        if not tasks:
            print("No tasks available to complete.")
        else:
            task_num = input("Enter the task number to mark as completed: ")
            if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                tasks[int(task_num) - 1]['Status'] = 'Completed'
                print(f"Task '{tasks[int(task_num) - 1]['Name']}' marked as completed.")
            else:
                print("Invalid task number.")
    elif choice == '6':
        print("Exiting the Smart Study Planner. Goodbye!")
        break
    else:
        continue
