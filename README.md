**1. Description of the Project:**

The mentioned code creates a straightforward Python To-Do List application with a graphical user interface supported by the Tkinter package. With features including adding tasks, changing task status, storing tasks to a JSON file, and loading tasks from the file, the application helps users schedule and keep track of their tasks.
1. Class Organisation: The application as a whole is represented by the main class, {TodoApp}.
   - The class integrates a Treeview widget to show tasks in a tabular manner and uses Tkinter for the graphical user interface elements.
   - It has functions to add tasks, update task status, show tasks in the Treeview, save tasks to a file, and load tasks from a JSON file.
2. GUI Components: - The GUI is built up of a main window with a title label, a task-displaying Treeview widget, and buttons for adding, editing, saving, and quitting tasks.
   - Task data including title, description, priority, due date, and status is displayed in columns in the Treeview.
   - To input task data or update task status, select the Add Task and Update Status buttons, which open new windows.
3. Styling: To enhance the application's visual appeal, unique fonts and styles are used.
   - Seguee UI Black, Cascadia Code SemiLight, Copperplate Gothic Bold, and Bahnschrift SemiBold are some of the fonts that were applied.
4. Data Persistence: - The `TodoApp` class maintains tasks as a list that is loaded from and saved to a JSON file titled `tasks.json}.
   - Reading from and writing to the file are handled by the `load_tasks` and `save_tasks` functions.
5. Task Management: - Tasks will appear as dictionaries with keywords with "title," "description," "due_date," "priority," and "status" serving as keys.
   - A other window enables users to set up tasks, and another one enables them to update the status of those tasks.
6. Main Execution: - When the script is run ({__name__ == "__main__"}), the application is executed.
   - It first initialises an instance of the `TodoApp} class and establishes a Tkinter root window.
Overall, the project provides a basic foundation for a To-Do List application with a graphical user interface in Python. Users can interact with the application to manage their tasks effectively.



**2. Instructions on how to set up and run the application:**

To set up and run the To-Do List application, follow these instructions:
Prerequisites:
1. Python: Ensure that Python is installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

Setup Steps:
1. Download the Code:
   - Download the provided Python script with the To-Do List application code. Save it to a directory of your choice.
2. Install Tkinter (if not already installed):
   - Tkinter is included with most Python installations. However, if you encounter issues or if Tkinter is not installed, you may need to install it. You can install Tkinter using the following command:
     ```bash
     pip install tk
     ```
3. Run the Application:
   - Open a terminal or command prompt.
   - Navigate to the directory where you saved the Python script (`todo_app.py`).
   - Run the script using the following command:
     ```bash
     python todo_app.py
     ```
   - This will launch the To-Do List application.
4. Interact with the Application:
   - The application window will appear, featuring a title label, a table displaying tasks, and buttons for adding tasks, updating task status, saving tasks, and exiting the application.
   - You can interact with the application by adding tasks, updating their status, saving the task list, and exiting the application using the provided buttons.
5. Task Persistence:
   - Tasks are saved to a file named `tasks.json` in the same directory as the script. This file will be automatically created if it doesn't exist. The tasks are loaded from this file when the application starts, ensuring that your task data is preserved between sessions.
6. Close the Application:
   - You can close the application by clicking the "Exit" button or closing the application window.
Following these steps should allow you to set up and run the To-Do List application on your system.



**Screenshots**
1. ![WebDev-1](https://github.com/Manognagrandhi/keka-techno_Mobile-Dev/assets/111331923/1f0613fc-3248-40d3-8bce-cbb4cb410ada)
2. 
