tasks = []

def addTask():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def ListTasks():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks):
            print(f"tasks {index}. {task}")


def DelTask():
        ListTasks()
        try:
            tasktodelete = int(input("Enter the task you want to delete: "))
            if tasktodelete >= 0 and tasktodelete < len(tasks):
                tasks.pop(tasktodelete)
                print(f"Task deleted successfully")
            else:
                print("Task not found.")
        except:
            print("Invalid input. Please try again.")
            return
    
    
if __name__ == '__main__':
    print("Welcome to do list")
    
    while True:
        print("\n Please select the following options: ")
        print("---------------------------------------")
        print("1. Enter a new task to list")
        print("2. Delete the task")
        print("3. Display the list")
        print("4. Exit")
        
        choice = input("Enter your choice : ")
        
        if(choice == "1"):
            addTask()
        
        elif(choice == "2"):
            DelTask()
        
        elif(choice == "3"):
            ListTasks()
           
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break  
            
        else:
            print("Invalid choice, please try again.")