tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet.\n")
    else:
        print("\nYour Tasks:")
        count = 1
        for task in tasks:
            print(str(count)  + task)
            count = count + 1
        print()


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!\n")


def delete_task():
    show_tasks()
    num = input("Enter task number to delete: ")
    if num.isdigit():
        index = int(num) - 1
        if index >= 0 and index < len(tasks):
            removed = tasks.pop(index)
            print("Deleted: " + removed + "\n")
        else:
            print("Invalid number.\n")
    else:
        print("Invalid input.\n")


while True:
    print("===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print(" GoodBye!")
        break
    else:
        print("Invalid choice.\n")