import json
import os


TASK_FILE = "tasks.json"


def load_tasks():
    """Load task from JSON file."""
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)
    
def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        
        
def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks available.")
        return   
    print("\n Your Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "Done" if task['done'] else "Not Done"
        print(f"{idx}. [{status}] {task['title']}")
        
# Main menu Loop
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark task as completed")
        print("4. Exit")
        
        
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            tasks.append({"title": title, "done": False})
            save_tasks(tasks)
        elif choice == "3":
            show_tasks
            if not tasks:
                continue      
            try:
                task_num = int(input("Enter task number to mark as complete: "))
                if 1<= task_num <= len(tasks):
                    tasks[task_num - 1] ["completed"] = True
                    save_tasks (tasks)
                    print("task Marked as complete")
                else:
                    print("Invalid task number")
            except ValueError:
                print("please enter a valid number")                   
        elif choice == "4" :
            print("Good Bye")
            break
        else:
            print("Invalid choice.")
            
            
if __name__ == "__main__":
    main()
