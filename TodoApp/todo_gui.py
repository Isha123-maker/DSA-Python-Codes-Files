import tkinter as tk
from tkinter import messagebox
from todo import TodoApp

class TodoGUI:
    def __init__(self, root):
        self.app = TodoApp()
        self.root = root
        self.root.title("Simple Todo App")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.entry = tk.Entry(self.frame, width=30)
        self.entry.grid(row=0, column=0, padx=5)
        self.add_btn = tk.Button(self.frame, text="Add Todo", command=self.add_todo)
        self.add_btn.grid(row=0, column=1, padx=5)

        self.listbox = tk.Listbox(self.frame, width=40)
        self.listbox.grid(row=1, column=0, columnspan=2, pady=5)

        self.complete_btn = tk.Button(self.frame, text="Complete", command=self.complete_todo)
        self.complete_btn.grid(row=2, column=0, pady=5)
        self.remove_btn = tk.Button(self.frame, text="Remove", command=self.remove_todo)
        self.remove_btn.grid(row=2, column=1, pady=5)

        self.refresh_list()

    def add_todo(self):
        title = self.entry.get().strip()
        if title:
            self.app.add_todo(title)
            self.entry.delete(0, tk.END)
            self.refresh_list()
        else:
            messagebox.showwarning("Input Error", "Todo title cannot be empty.")

    def complete_todo(self):
        idx = self.listbox.curselection()
        if idx:
            self.app.complete_todo(idx[0])
            self.refresh_list()
        else:
            messagebox.showwarning("Selection Error", "Select a todo to complete.")

    def remove_todo(self):
        idx = self.listbox.curselection()
        if idx:
            self.app.remove_todo(idx[0])
            self.refresh_list()
        else:
            messagebox.showwarning("Selection Error", "Select a todo to remove.")

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for todo in self.app.list_todos():
            status = "✔" if todo.completed else "✗"
            self.listbox.insert(tk.END, f"{status} {todo.title}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = TodoGUI(root)
    root.mainloop()
