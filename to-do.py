import os

# Function to display the menu
def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

# Function to view tasks
def view_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour To-Do List:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task.strip()}")
            else:
                print("Your To-Do list is empty.")
    else:
        print("No tasks file found. Start by adding a task.")

# Function to add a task
def add_task():
    task = input("\nEnter the task you want to add: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added successfully.")

# Function to delete a task
def delete_task():
    view_tasks()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as e:
        print(f"Error: {e}")

# Main function to run the program
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1/2/3/4): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye! Your to-do list has been saved.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()

