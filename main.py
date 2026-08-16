from storage import load_tasks
from tasks import add_task, view_tasks, complete_task, delete_task


def main_menu():
    print("==== Smart Study Planner ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    try:
        choice = input("Please enter your choice (1-5): ").strip()
        return choice
    except (EOFError, KeyboardInterrupt):
        print("\nInput interrupted. Please try again.")
        return ""
    except Exception as e:
        print(f"Unexpected error reading input: {e}")
        return ""


def main():
    try:
        tasks = load_tasks()
    except Exception as e:
        print(f"Error loading tasks: {e}")
        print("Starting with empty task list.")
        tasks = []

    while True:
        try:
            choice = main_menu()

            # Adding tasks
            if choice == "1":
                try:
                    add_task(tasks)
                except Exception as e:
                    print(f"Error adding task: {e}")

            # Viewing tasks
            elif choice == "2":
                try:
                    view_tasks(tasks)
                except Exception as e:
                    print(f"Error viewing tasks: {e}")

            # Marking tasks as completed
            elif choice == "3":
                try:
                    complete_task(tasks)
                except Exception as e:
                    print(f"Error completing task: {e}")

            # Deleting tasks
            elif choice == "4":
                try:
                    delete_task(tasks)
                except Exception as e:
                    print(f"Error deleting task: {e}")

            # Exiting the program
            elif choice == "5":
                print("Exiting the Smart Study Planner. Goodbye!")
                break

            elif choice == "":
                print("Empty choice. Please try again.")

            else:
                print("Invalid choice. Please try again.")

        except KeyboardInterrupt:
            print("\nProgram interrupted by user. Exiting gracefully.")
            break
        except Exception as e:
            print(f"Unexpected error in main loop: {e}")
            print("Continuing with program...")

if __name__ == "__main__":
    main()
