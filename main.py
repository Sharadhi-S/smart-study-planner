from storage import load_tasks
from tasks import add_task, view_tasks, complete_task, delete_task


def main_menu():
    print("==== Smart Study Planner ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Please enter your choice (1-5): ").strip()
    return choice


def main():
    global tasks
    tasks = load_tasks()


    while True:
        choice = main_menu()

        # Adding tasks
        if choice == "1":
            add_task(tasks)

        # Viewing tasks
        elif choice == "2":
            view_tasks(tasks)

        # Marking tasks as completed
        elif choice == "3":
            complete_task(tasks)

        # Deleting tasks
        elif choice == "4":
            delete_task(tasks)

        # Exiting the program
        elif choice == "5":
            print("Exiting the Smart Study Planner. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
