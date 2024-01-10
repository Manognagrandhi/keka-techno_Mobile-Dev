
import json
import datetime
import tkinter as tk
from tkinter import ttk


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = self.load_tasks()

        custom_font = ("Segoe UI Black", 11)  # Change the font family and size
        custom_font1 = ("Cascadia Code SemiLight", 11)
        custom_font2 = ("Copperplate Gothic Bold", 13)
        background_color="#FFFF00"

        fontstyle=ttk.Style()
        fontstyle.configure('Custom.Treeview',font=custom_font1)
        fontstyle.configure('Custom.Treeview.Heading',font=custom_font)

        self.title_label = ttk.Label(root, text="To-Do List", font=("Bahnschrift SemiBold", 20),background=background_color)
        self.title_label.grid(row=0, column=0, columnspan=4, pady=(10, 0))

        self.tree = ttk.Treeview(root, columns=('Title', 'Description', 'Due Date', 'Priority', 'Status'),
                                 show='headings',style="Custom.Treeview")
        self.tree.heading('Title', text='Title', anchor='center')
        self.tree.heading('Description', text='Description', anchor='center')
        self.tree.heading('Due Date', text='Due Date', anchor='center')
        self.tree.heading('Priority', text='Priority', anchor='center')
        self.tree.heading('Status', text='Status', anchor='center')
        self.tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.display_tasks()

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=2, column=0, padx=10, pady=(0, 10), sticky='w')
        self.add_button.configure(style='Custom.TButton')

        self.update_button = ttk.Button(root, text="Update Status", command=self.update_status)
        self.update_button.grid(row=2, column=1, padx=10, pady=(0, 10), sticky='w')
        self.update_button.configure(style='Custom.TButton')

        self.save_button = ttk.Button(root, text="Save", command=self.save_tasks)
        self.save_button.grid(row=2, column=2, padx=10, pady=(0, 10), sticky='w')
        self.save_button.configure(style='Custom.TButton')

        self.exit_button = ttk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.grid(row=2, column=3, padx=10, pady=(0, 10), sticky='e')
        self.exit_button.configure(style='Custom.TButton')

        style=ttk.Style()
        style.configure('Custom.TButton',font=custom_font2)

    def load_tasks(self):
        try:
            with open('tasks.json', 'r') as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        for task in self.tree.get_children():
            self.tree.delete(task)

        for task in self.tasks:
            self.tree.insert('', 'end', values=(task['title'], task['description'], task['due_date'],
                                                task['priority'], task['status']))

    def add_task(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Add Task")

        tk.Label(add_window, text="Title:", font=("Copperplate Gothic Bold", 12)).grid(row=0, column=0, padx=10, pady=5, sticky='w')
        title_entry = tk.Entry(add_window)
        title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Description:", font=("Copperplate Gothic Bold", 12)).grid(row=1, column=0, padx=10, pady=5, sticky='w')
        description_entry = tk.Entry(add_window)
        description_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Due Date (YYYY-MM-DD):", font=("Copperplate Gothic Bold", 12)).grid(row=2, column=0, padx=10, pady=5,
                                                                                     sticky='w')
        due_date_entry = tk.Entry(add_window)
        due_date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(add_window, text="Priority:", font=("Copperplate Gothic Bold", 12)).grid(row=3, column=0, padx=10, pady=5, sticky='w')
        priority_entry = ttk.Combobox(add_window, values=['Low', 'Medium', 'High'])
        priority_entry.grid(row=3, column=1, padx=10, pady=5)
        priority_entry.set('Low')

        tk.Button(add_window, text="Add Task", command=lambda: self.add_task_to_list(title_entry.get(),
                                                                                     description_entry.get(),
                                                                                     due_date_entry.get(),
                                                                                     priority_entry.get(),
                                                                                     add_window),
                  font=("Copperplate Gothic Bold", 12)).grid(row=4, column=0, columnspan=2, pady=10)

    def add_task_to_list(self, title, description, due_date, priority, add_window):
        task = {
            'title': title,
            'description': description,
            'due_date': due_date,
            'priority': priority,
            'status': 'New'
        }

        self.tasks.append(task)
        self.save_tasks()
        self.display_tasks()
        add_window.destroy()

    def update_status(self):
        selected_item = self.tree.selection()

        if not selected_item:
            return

        update_window = tk.Toplevel(self.root)
        update_window.title("Update Status")

        tk.Label(update_window, text="New Status:", font=("Copperplate Gothic Bold", 12)).grid(row=0, column=0, padx=10, pady=5,
                                                                             sticky='w')
        status_entry = ttk.Combobox(update_window, values=['New', 'In Progress', 'Completed'])
        status_entry.grid(row=0, column=1, padx=10, pady=5)
        status_entry.set(self.tree.item(selected_item, 'values')[-1])

        tk.Button(update_window, text="Update Status", command=lambda: self.update_task_status(selected_item[0],
                                                                                               status_entry.get(),
                                                                                               update_window),
                  font=("Arial", 12)).grid(row=1, column=0, columnspan=2, pady=10)

    def update_task_status(self, task_id, new_status, update_window):
        for task in self.tasks:
            if task['title'] == self.tree.item(task_id, 'values')[0]:
                task['status'] = new_status
                break

        self.save_tasks()
        self.display_tasks()
        update_window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()