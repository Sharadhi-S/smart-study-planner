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

while True:
    choice = main_menu()
    print(f"You selected option {choice}.")
    if choice == '6':
        print("Exiting the Smart Study Planner. Goodbye!")
        break
    else:
        continue
