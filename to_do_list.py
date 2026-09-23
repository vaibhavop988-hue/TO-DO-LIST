tasks= []
 
def display_menu():
    print("\nTO-DO LIST MENU")
    print("1.Add Task")
    print("2.View Tasks")
    print("3.Mark Task as Done")
    print("4.Remove Task")
    print("5.Exit")
 
 
def add_a_task():
    task = input("Enter the task: ")
    tasks.append({"task":task, "done":False})
    print(f"Task added:{task}")


def view_all_tasks():
    if not tasks:
        print("No tasks yet!")
        return
    print("\nYour Tasks:")
    for index,task in enumerate(tasks,start=1):
        status = "done" if task["done"] else "not done"
        print(f"{index}. {task['task']} : {status}")


def mark_as_done():
    view_all_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number to be marked as done: ")) - 1
        if 0<= task_index <len(tasks):
            tasks[task_index]["done"] = True
            print(f"Task '{tasks[task_index]['task']}' marked as done.")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")


def remove_a_task():
    view_all_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter the task number that you want to remove:")) - 1
        if 0<= task_index < len(tasks):
            remove = tasks.pop(task_index)
            print(f"Removed task: {remove['task']}")
        else:
            print("Invalid number!")
    except ValueError:
        print("Please enter a valid number.")
    

while True:
    display_menu()
    choice = input("choose a number (1-5):")
    if choice == "1":
        add_a_task()
    elif choice == "2":
        view_all_tasks()
    elif choice == "3":
        mark_as_done()
    elif choice == "4":
        remove_a_task()
    elif choice == "5":
        print("Exit")
        break
    else:
        print("Invalid choice!")



        

