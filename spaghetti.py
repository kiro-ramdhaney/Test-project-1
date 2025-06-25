import json
import os

TODO_FILE = "todo.json"

# Load existing tasks or initialize an empty list
def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
        return

    print("\n📝 To-Do List:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task['completed'] else " "
        print(f"{i}. [{status}] {task['title']}")

def add_task(tasks):
    title = input("Enter a new task: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("No task entered.")

def complete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as complete: "))
        tasks[num - 1]['completed'] = True
        save_tasks(tasks)
        print("Task marked as complete.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_task(tasks):
    show_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do CLI Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
