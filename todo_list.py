def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as done")
    print("5. Exit")

def show_tasks(tasks):
    if not tasks:
        print("No tasks in your list.")
    else:
        for i, (task, done) in enumerate(tasks, 1):
            status = "✓" if done else "✗"
            print(f"{i}. [{status}] {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append((task, False))
    print("Task added.")

def remove_task(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed task: {removed[0]}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done(tasks):
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            task, _ = tasks[index]
            tasks[index] = (task, True)
            print(f"Marked '{task}' as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            mark_done(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()