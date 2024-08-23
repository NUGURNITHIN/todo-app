# To-Do App in Python

# Initialize an empty list to store tasks
tasks = []

def add_task(task):
    """Add a task to the to-do list."""
    tasks.append({"task": task, "completed": False})
    print(f"Task '{task}' added.")

def view_tasks():
    """View all tasks in the to-do list."""
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        for index, task in enumerate(tasks):
            status = "✓" if task["completed"] else "✗"
            print(f"{index + 1}. {task['task']} [{status}]")

def mark_task_as_done(task_number):
    """Mark a specific task as done."""
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        print(f"Task '{tasks[task_number - 1]['task']}' marked as completed.")
    else:
        print("Invalid task number.")

def remove_task(task_number):
    """Remove a specific task from the to-do list."""
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Task '{removed_task['task']}' removed.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the to-do app."""
    while True:
        print("\nTo-Do List Options:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_number = int(input("Enter the task number to mark as done: "))
            mark_task_as_done(task_number)
        elif choice == '4':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_number)
        elif choice == '5':
            print("Exiting the to-do app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
