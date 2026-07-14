import json 

def main_menu():
    print("==== Smart Study Planner ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Save Tasks")
    print("6. Exit")

    choice = input("Please enter your choice (1-6): ").strip()
    return choice

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved successfully")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

tasks = load_tasks()

while True:
    choice = main_menu()
    
    # Adding tasks
    if choice == '1':
        task = input("Enter the task description: ").title().strip()
        if task=="":
            print("Task description cannot be empty.")
            continue
        else:
            tasks.append({"Name": task, "Status": "Pending"})
            print(f"Task '{task}' added.")
    
    # Viewing tasks
    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                print(f"{idx}. {task['Name']} - {task['Status']}")
    
    # Marking tasks as completed
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
    
    # Deleting tasks
    elif choice == '4':
        if not tasks:
            print("No tasks available to delete.")
        else:
            task_num = input("Enter the task number to delete: ")
            confirm = input("Are you sure you want to delete this task? (y/n): ")
            if confirm.lower() == 'n':
                print("Task deletion cancelled.")
            else:
                if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                    removed_task = tasks.pop(int(task_num) - 1)
                    print(f"Task '{removed_task['Name']}' deleted.")
                else:
                    print("Invalid task number.")

    # Saving tasks to a file
    elif choice == '5':
        save_tasks()


    # Exiting the program            
    elif choice == '6':
        print("Exiting the Smart Study Planner. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
