from storage import save_tasks


def add_task(tasks):
    task = input("Enter the task description: ").strip()
    if task == "":
        print("Task description cannot be empty.")
    else:
        tasks.append({"Name": task, "Status": "Pending"})
        save_tasks(tasks)
        print(f"Task '{task}' added.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['Name']} - {task['Status']}")


def complete_task(tasks):
    if not tasks:
        print("No tasks available to complete.")
    else:
        task_num = input("Enter the task number to mark as completed: ")
        if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
            index = int(task_num) - 1
            tasks[index]["Status"] = "Completed"
            save_tasks(tasks)
            print(f"Task '{tasks[index]['Name']}' marked as completed.")
        else:
            print("Invalid task number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
    else:
        task_num = input("Enter the task number to delete: ")
        confirm = input("Are you sure you want to delete this task? (y/n): ")
        if confirm.lower() == "n":
            print("Task deletion cancelled.")
        else:
            if task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                index = int(task_num) - 1
                removed_task = tasks.pop(index)
                save_tasks(tasks)
                print(f"Task '{removed_task['Name']}' deleted.")
            else:
                print("Invalid task number.")
