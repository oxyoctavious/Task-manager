import json
import os
from colorama import init, Fore, Style
init(autoreset=True)

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
        
    tasks =sorted(tasks, key=lambda x: x.get("completed", False))    
def show_tasks(tasks):
    """Display all tasks. 
    
    Display all tasks in the list with their completion status.

    Shows a numbered list of tasks, each marked as:
    - ✅ Done if the task is completed
    - ❌ Not Done if the task is still pending
    """
    if not tasks:
        print( Fore.YELLOW + "No tasks available.")
        return   
    task = sorted(tasks, key=lambda x: x.get("completed", False))

    total= len(tasks)
    completed = sum(1 for t in tasks if t["completed"])
    pending = total - completed
    print(Fore.CYAN + "\n Your Tasks: ")
    
    
    for idx, task in enumerate(tasks, start=1):
        status = (Fore.GREEN + "✅ Done") if task["completed"] else (Fore.BLUE + "❌ Not Done")
        title = Style.DIM + task['title'] if task["completed"] else Fore.YELLOW + task['title']
        print(f"{idx}. [{status}] {title}")
       
        
        
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
                task_num = int(input("Enter task number to Delete: "))
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
