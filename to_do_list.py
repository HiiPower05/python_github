# + if list is empty

tasks = []

# add
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    return tasks

# delete
def delete_task():
    task = input("Enter a task to delete: ")
    tasks.remove(task)
    return tasks

# list
def print_tasks():
    print("LIST")
    task_list = [print(f"{t}") for t in tasks]

while True:
    print("----- TO DO LIST -----")
    print("1.Add task\n2.Delete\n3.Show tasks\n4.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        delete_task()
    elif choice == "3":
        print_tasks()
    elif choice == "4":
        print("Exiting...")
        break