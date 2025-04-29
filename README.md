# To-Do List

A simple command-line To-Do List application built using Python. This program allows users to view, add, and delete tasks from a text-based to-do list. The tasks are saved in a file (`tasks.txt`) so that they persist across program runs.

## Features

- **View Tasks**: Displays the current list of tasks.
- **Add Task**: Allows the user to add a new task to the to-do list.
- **Delete Task**: Allows the user to remove a specific task from the list.
- **Persistent Storage**: Tasks are saved to a text file (`tasks.txt`) and persist between program executions.

## Requirements

- Python 3.x installed.

## How It Works

The program offers a simple menu with four options. The user can choose to view, add, or delete tasks, or exit the program. The tasks are stored in a text file, and every time the program is run, it loads the tasks from the file and allows the user to interact with them.

### Menu Options

1. **View Tasks**: Displays the list of tasks.
2. **Add Task**: Adds a new task to the list.
3. **Delete Task**: Deletes a task from the list based on its number.
4. **Exit**: Exits the program and saves the tasks.

## Running the Project

1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the script using the following command:

   ```python 
   python3 todo_list.py
   ```
4. Follow the on-screen instructions to interact with your to-do list.

## Example Usage
## Start the Program

    To-Do List Menu:
    1. View Tasks
    2. Add Task
    3. Delete Task
    4. Exit
    Choose an option (1/2/3/4): 2
    Enter the task you want to add: Buy groceries
    Task 'Buy groceries' added successfully.

## View Tasks

    To-Do List Menu:
    1. View Tasks
    2. Add Task
    3. Delete Task
    4. Exit
    Choose an option (1/2/3/4): 1

    Your To-Do List:
    1. Buy groceries

## Delete Task

    To-Do List Menu:
    1. View Tasks
    2. Add Task
    3. Delete Task
    4. Exit
    Choose an option (1/2/3/4): 3
    Your To-Do List:
    1. Buy groceries
    Enter the task number to delete: 1
    Task deleted successfully.

## Exit the Program

    To-Do List Menu:
    1. View Tasks
    2. Add Task
    3. Delete Task
    4. Exit
    Choose an option (1/2/3/4): 4
    Goodbye! Your to-do list has been saved.


## Future Enhancements
-**Edit Task**: Add the ability to modify existing tasks.
-**Prioritize Tasks**: Allow users to prioritize tasks.
-**Graphical User Interface (GUI)**: Add a GUI using Tkinter or another framework.

## License
This project is open-source and available under the MIT License.