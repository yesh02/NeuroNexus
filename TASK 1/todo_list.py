import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import json

class CoolTodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cool To-Do List App")
        self.root.geometry("400x300")

        self.style = ttk.Style()
        self.style.theme_use("clam")  # You can try other themes like "winnative", "alt", etc.

        self.todo_list = self.load_todo_list()

        self.task_var = tk.StringVar()
        self.task_entry = ttk.Entry(root, textvariable=self.task_var, width=30)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = ttk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        self.task_listbox = tk.Listbox(root, height=8, width=40, borderwidth=0, selectbackground="#a6a6a6", selectforeground="black")
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.remove_button = ttk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.load_tasks_to_listbox()

    def load_todo_list(self):
        try:
            with open("cool_todo_list.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_todo_list(self):
        with open("cool_todo_list.json", "w") as file:
            json.dump(self.todo_list, file, indent=2)

    def load_tasks_to_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list:
            self.task_listbox.insert(tk.END, f"{task['title']} - {task['date']}")

    def add_task(self):
        title = self.task_var.get()
        if title:
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            task = {"title": title, "date": date}
            self.todo_list.append(task)
            self.save_todo_list()
            self.load_tasks_to_listbox()
            self.task_var.set("")  # Clear the entry field after adding a task
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            removed_task = self.todo_list.pop(task_index)
            self.save_todo_list()
            self.load_tasks_to_listbox()
            messagebox.showinfo("Task Removed", f"Task '{removed_task['title']}' removed.")
        else:
            messagebox.showwarning("Warning", "Please select a task to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CoolTodoApp(root)
    root.mainloop()
