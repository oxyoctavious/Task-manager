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
    """Display all tasks. 
    
    Display all tasks in the list with their completion status.

    Shows a numbered list of tasks, each marked as:
    - ✅ Done if the task is completed
    - ❌ Not Done if the task is still pending
    """
    if not tasks:
        print("No tasks available.")
        return   
    print("\n Your Tasks:")
    for idx, task in enumerate(tasks, start=1):
        status = "✅ Done" if task["completed"] else "❌Not Done"
        print(f"{idx}. [{status}] {task['title']}")
        
        # Main menu Loop
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark task as completed")
        print("4. Delete a task")
        print("5. Exit")
        
        
        choice = input("Choose an option: ")
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            title = input("Enter task title: ")
            tasks.append({"title": title, "completed": False})
            save_tasks(tasks)
            print("Task added")
        elif choice == "3":
            # we have to call the show_tasks function so instad of typing just show_tasks we have to call it as show_tasks()
            show_tasks (tasks)
            if not tasks:
                continue      
            try:
                task_num = int(input("Enter task number to mark as complete: "))
                # len(tasks) is meant to the total numbers of tasks 
                # so it checks the if the entered task num is valid or not
                if 1<= task_num <= len(tasks):
                    tasks[task_num - 1] ["completed"] = True
                    # task_num - 1 means the the list starts from zero so the actual place of the first task is 0
                    # so this line makes the entered number according to the list 
                    save_tasks (tasks)
                    print("✅ Task marked as completed!")
                else:
                    print("Invalid task number")
            except ValueError:
                print("Please enter a valid number") 
        elif choice == "4":
            show_tasks(tasks)
            if not tasks:
                continue
            try:
                task_num = int(input("Enter task number to mark as complete"))
                if 1<= task_num <= len(tasks):
                    delete_tasks = tasks.pop (task_num-1)  
                    save_tasks(tasks)
                    print(f"Deleted task: {delete_tasks['title']}") 
                else: 
                    print("Invalid task number")
            except ValueError:
                print("Please enter valid task number")
                                  
        elif choice == "5" :
            print("Good Bye")
            break
        else:
            print("Invalid choice.")
            
            
if __name__ == "__main__":
    main()
