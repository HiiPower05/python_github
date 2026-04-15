# + if list is empty

# File handling: Create file, save file, load file
tasks = []

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

    task = input("Enter a task to delete: ")
    tasks.remove(task)
    return tasks
# no tasks to delete

# list
def view_tasks():
    if tasks:
        print("\n TO-DO")
        for index, task in enumerate(tasks, start=1):
            mark = "✔" if task['Completed'] else ''
            print(f"{index}. {task['task']}{mark}")
    else:
        print("There are no tasks added.")

def main():
    while True:
        print("----- TO DO LIST -----")
        print("1.Add task | 2.Delete | 3.Show tasks | 4.Exit")
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
            print("Exiting...")
            break

if __name__ == "__main__":
    main()

