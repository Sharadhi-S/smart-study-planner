from storage import save_tasks


def add_task(tasks):
    try:
        task = input("Enter the task description: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted. Task addition cancelled.")
        return
    except Exception as e:
        print(f"Error reading input: {e}")
        return

    if task == "":
        print("Task description cannot be empty.")
    else:
        try:
            tasks.append({"Name": task, "Status": "Pending"})
            if save_tasks(tasks):
                print(f"Task '{task}' added.")
            else:
                print("Failed to save task.")
        except Exception as e:
            print(f"Error adding task: {e}")


def view_tasks(tasks):
    try:
        if not tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for idx, task in enumerate(tasks, start=1):
                try:
                    print(f"{idx}. {task['Name']} - {task['Status']}")
                except (KeyError, TypeError) as e:
                    print(f"{idx}. [Invalid task data] - Error: {e}")
    except Exception as e:
        print(f"Error viewing tasks: {e}")


def complete_task(tasks):
    if not tasks:
        print("No tasks available to complete.")
    else:
        try:
            task_num = input("Enter the task number to mark as completed: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Task completion cancelled.")
            return
        except Exception as e:
            print(f"Error reading input: {e}")
            return

        try:
            if task_num and task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                index = int(task_num) - 1
                tasks[index]["Status"] = "Completed"
                if save_tasks(tasks):
                    print(f"Task '{tasks[index]['Name']}' marked as completed.")
                else:
                    print("Failed to save changes.")
            else:
                print("Invalid task number.")
        except (ValueError, IndexError, KeyError) as e:
            print(f"Error processing task number: {e}")
        except Exception as e:
            print(f"Error completing task: {e}")


def delete_task(tasks):
    if not tasks:
        print("No tasks available to delete.")
    else:
        try:
            task_num = input("Enter the task number to delete: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nInput interrupted. Task deletion cancelled.")
            return
        except Exception as e:
            print(f"Error reading input: {e}")
            return

        try:
            if task_num and task_num.isdigit() and 1 <= int(task_num) <= len(tasks):
                index = int(task_num) - 1
                try:
                    confirm = input(f"Are you sure you want to delete '{tasks[index]['Name']}'? (y/n): ")
                except (EOFError, KeyboardInterrupt):
                    print("\nInput interrupted. Task deletion cancelled.")
                    return
                except Exception as e:
                    print(f"Error reading confirmation: {e}")
                    return

                try:
                    if confirm.lower() == "n":
                        print("Task deletion cancelled.")
                        return
                except AttributeError:
                    print("Invalid confirmation format. Assuming 'yes' to continue.")

                try:
                    removed_task = tasks.pop(index)
                    if save_tasks(tasks):
                        print(f"Task '{removed_task['Name']}' deleted.")
                    else:
                        print("Failed to delete task.")
                        tasks.insert(index, removed_task)  # Restore the task
                except (IndexError, KeyError) as e:
                    print(f"Error deleting task: {e}")
                except Exception as e:
                    print(f"Unexpected error during deletion: {e}")
            else:
                print("Invalid task number.")
        except (ValueError, IndexError) as e:
            print(f"Error processing task number: {e}")
        except Exception as e:
            print(f"Error deleting task: {e}")
