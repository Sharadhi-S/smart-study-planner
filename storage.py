import json


def save_tasks(tasks):
    try:
        # Validate input data
        if not isinstance(tasks, list):
            print("Error: tasks must be a list")
            return False

        # Validate each task in the list
        for i, task in enumerate(tasks):
            if not isinstance(task, dict):
                print(f"Error: task at index {i} must be a dictionary")
                return False
            if "Name" not in task or "Status" not in task:
                print(f"Error: task at index {i} must have 'Name' and 'Status' keys")
                return False

        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    except (IOError, OSError) as e:
        print(f"Error saving tasks (file operation): {e}")
        return False
    except (TypeError, ValueError) as e:
        print(f"Error saving tasks (data serialization): {e}")
        return False
    except Exception as e:
        print(f"Unexpected error saving tasks: {e}")
        return False
    return True

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            data = json.load(file)

            # Validate the loaded data
            if not isinstance(data, list):
                print("Warning: Invalid data format in tasks.json. Starting with empty list.")
                return []

            # Validate each task structure
            valid_tasks = []
            for task in data:
                if isinstance(task, dict) and "Name" in task and "Status" in task:
                    valid_tasks.append(task)
                else:
                    print("Warning: Skipping invalid task data")

            return valid_tasks

    except FileNotFoundError:
        # This is expected on first run - no file exists yet
        return []
    except json.JSONDecodeError as e:
        print(f"Warning: Corrupted task file. Starting with empty list. Error: {e}")
        return []
    except (IOError, OSError) as e:
        print(f"Error reading tasks file: {e}")
        return []
    except Exception as e:
        print(f"Unexpected error loading tasks: {e}")
        return []
