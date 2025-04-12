import tkinter as tk
import json

# Global task dictionary
tasks = {}

# Load tasks from file
def load_tasks():
    global tasks
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}

# Save tasks to file
def save_tasks():
    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)

# Clear the window
def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

# Main menu
def main_menu():
    clear_frame()
    label = tk.Label(window, text="Main Menu", font=('Poppins', 25))
    label.pack(pady=10)

    tk.Button(window, text="Add a Task", command=addTask, width=20, font=('Poppins', 16)).pack(pady=10)
    # tk.Button(window, text="View a Task", command=viewTask, width=20, font=('Poppins', 16)).pack(pady=10)
    # tk.Button(window, text="Update a Task", command=updateTask, width=20, font=('Poppins', 16)).pack(pady=10)
    # tk.Button(window, text="Delete a Task", command=deleteTask, width=20, font=('Poppins', 16)).pack(pady=10)

# Add task functionality
def addTask():
    clear_frame()
    window.geometry("700x500")
    tk.Label(window, text="Add a Task", font=('Poppins', 25)).pack(pady=10)

    frame = tk.Frame(window)

    tk.Label(frame, text="Task name:", font=('Poppins', 16)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    taskname_entry = tk.Entry(frame, font=('Poppins', 16))
    taskname_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(frame, text="Task description:", font=('Poppins', 16)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    taskdesc_entry = tk.Entry(frame, font=('Poppins', 16))
    taskdesc_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(frame, text="Task priority:", font=('Poppins', 16)).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    taskpriority_entry = tk.Entry(frame, font=('Poppins', 16))
    taskpriority_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(frame, text="Task due date:", font=('Poppins', 16)).grid(row=3, column=0, padx=10, pady=10, sticky="w")
    taskduedate_entry = tk.Entry(frame, font=('Poppins', 16))
    taskduedate_entry.grid(row=3, column=1, padx=10, pady=10)

    def submit():
        name = taskname_entry.get()
        desc = taskdesc_entry.get()
        priority = taskpriority_entry.get()
        due = taskduedate_entry.get()

        if name in tasks:
            tk.messagebox.showerror("Error", "Task already exists!")
            return
        if priority.lower() not in ["high", "medium", "low"]:
            tk.messagebox.showerror("Error", "Invalid priority. Must be high/medium/low")
            return

        tasks[name] = {
            "description": desc,
            "priority": priority,
            "due_date": due
        }
        save_tasks()
        tk.messagebox.showinfo("Success", "Task added successfully")
        main_menu()

    tk.Button(frame, text="Submit", command=submit, width=20, font=('Poppins', 16)).grid(row=4, column=1, padx=10, pady=10)
    tk.Button(frame, text="Back to Menu", command=main_menu, width=20, font=('Poppins', 16)).grid(row=4, column=0, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

# Load existing tasks at startup
load_tasks()

# Create main window
window = tk.Tk()
window.geometry("700x500")
window.title("Task Manager")

main_menu()
window.mainloop()
