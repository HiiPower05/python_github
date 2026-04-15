# File handling: Create file, save file, load file
import json
tasks = []
filename = "tasks.json"

def load_tasks():
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
            print(f"{len(tasks)} tasks from {filename}")
    except FileNotFoundError:
        tasks = []
        print("No previous tasks found. Starting again...")
    except json.JSONDecodeError:
        tasks = []
        print("File corrupted. Starting again...")

def save_tasks():
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)
    print(f"Tasks saved to {filename}.")

# add
def add_task(task):
    if task and task.strip():
        tasks.append({
            "task":task, 'Completed': False
        })
        print('Task added successfully')
    else:
        print("Please enter a task")

# delete
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        task = int(input("Enter a task number to delete: "))
        tasks.pop(task-1)
        print(f"Task Removed: {task}")
    except ValueError:
        print("Please enter a number")

# list
def view_tasks():
    if tasks:
        print("\n TO-DO")
        for index, task in enumerate(tasks, start=1):
            mark = "✔" if task['Completed'] else ''
            print(f"{index}. {task['task']}{mark}")
    else:
        print("There are no tasks added.")

def completed_tasks():
    view_tasks()
    if not tasks:
        return

    index = int(input("Enter task number: "))
    if 1 <= index <= len(tasks):
        tasks[index-1]['Completed'] = True
        print(f"Marked as completed: {tasks[index-1]['task']}")
    else:
        print("Invalid task number. Try again.")

def main():
    load_tasks()

    while True:
        print("----- TO DO LIST -----")
        print("1.Add task | 2.Delete | 3.Show tasks | 4.Completed | 5. Exit | 6.Load")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Oops! That was no valid number. Try again...")
            continue

        # exception ValueError
        if choice == 1:
            task = input('Enter task: ').strip()
            add_task(task)
        elif choice == 2:
            delete_task()
        elif choice == 3:
            view_tasks()
        elif choice == 4:
            completed_tasks()
        elif choice == 5:
            save_tasks()
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

