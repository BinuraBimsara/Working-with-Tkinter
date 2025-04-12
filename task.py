import tkinter as tk
from tkinter import messagebox
import json
tasks={}

def save_tasks():
    with open("data.json", "w") as file:
        json.dump(tasks, file, indent=4)  # Write JSON to file

def load_tasks():
    """Loads tasks from a JSON file if it exists"""
    global tasks
    try:
        with open("data.json", "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = {}  # Initialize an empty dictionary if file doesn't exist

def addTask():
    clear_frame()
    window.geometry("700x500")
    label = tk.Label(window, text="Add a Task", font=('Poppins', 25))
    label.pack(pady=10)

    frame = tk.Frame(window)
    taskname_label = tk.Label(frame, text = "Task name : ", font = (("Poppins)", 16)))
    taskname_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    taskname_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    taskname_entry.grid(row=0, column=1, padx=10, pady=10)

    taskdesc_label = tk.Label(frame, text = "Task description : ", font = (("Poppins)", 16)))
    taskdesc_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
    taskdesc_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    taskdesc_entry.grid(row=1, column=1, padx=10, pady=10)

    taskpriority_label = tk.Label(frame, text = "Task priority : ", font = (("Poppins)", 16)))
    taskpriority_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    taskpriority_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    taskpriority_entry.grid(row=2, column=1, padx=10, pady=10)

    taskduedate_label = tk.Label(frame, text = "Task due date : ", font = (("Poppins)", 16)))
    taskduedate_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    taskduedate_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    taskduedate_entry.grid(row=3, column=1, padx=10, pady=10)

    def add():
        name = taskname_entry.get().lower()
        desc = taskdesc_entry.get()
        priority = taskpriority_entry.get()
        due = taskduedate_entry.get()

        if name in tasks:
            messagebox.showerror("Error", "Task already exists!")
            return
        if priority.lower() not in ["high", "medium", "low"]:
            messagebox.showerror("Error", "Invalid priority. Must be high/medium/low")
            return

        tasks[name] = {
            "description": desc,
            "priority": priority,
            "due_date": due
        }
        save_tasks()
        messagebox.showinfo("Success", "Task added successfully")
        addTask()

    submit_btn = tk.Button(frame, text="Add",command=add, width=10, font=('Poppins', 16))
    submit_btn.grid(row=4, column=1,padx=10, pady=10)

    backtoMenu_btn = tk.Button(frame, text = "Back to Menu",command=main_menu, width=15, font=('Poppins', 16))
    backtoMenu_btn.grid(row=4, column=0, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

def viewTask():
    clear_frame()
    window.geometry("700x500")
    label = tk.Label(window, text="View a Task", font=('Poppins', 25))
    label.pack(pady=10)

    frame = tk.Frame(window)
    taskname_label = tk.Label(frame, text = "Task name : ", font = (("Poppins)", 16)))
    taskname_label.grid(sticky="w",row=0, column=0, padx=10, pady=10)

    taskname_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    taskname_entry.grid(row=0, column=1, padx=10, pady=10)

    viewtask_text = tk.Text(frame,width=45, height=8, font = (("Poppins)", 16)))
    viewtask_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    viewtask_btn = tk.Button(frame, text="View Task", width=20, font=('Poppins', 16), command=lambda: handle_view_task(taskname_entry.get().lower(), viewtask_text))
    viewtask_btn.grid(row=2, column=1,padx=10, pady=10)  #Lambda is used to pass arguments.

    backtoMenu_btn = tk.Button(frame, text = "Back to Menu",command=main_menu, width=20, font=('Poppins', 16))
    backtoMenu_btn.grid(row=2, column=0, padx=10, pady=10)
    frame.pack(padx=10, pady=10)

def handle_view_task(task_name, output_widget):
    load_tasks()
    output_widget.delete("1.0", tk.END)  # Clear the Textbocx
    task = tasks.get(task_name)
    if task:
        output_widget.insert(tk.END,
            f"Task Name   : {task_name}\n"
            f"Description : {task['description']}\n"
            f"Priority    : {task['priority']}\n"
            f"Due Date    : {task['due_date']}\n"
        )
    else:
        output_widget.insert(tk.END, "Task not found.")

def updateTask():
    clear_frame()
    window.geometry("700x700")
    label = tk.Label(window, text="Update a Task", font=('Poppins', 25))
    label.pack(pady=10)

    frame = tk.Frame(window)
    updatename_label = tk.Label(frame, text="Task name : ", font = (("Poppins)", 16)))
    updatename_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    updatename_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    updatename_entry.grid(row=0, column=1, padx=10, pady=10)

    updatetask_text = tk.Text(frame,width=45, height=8, font = (("Poppins)", 16)))
    updatetask_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    viewtask_btn = tk.Button(frame, text="Find Task", width=15, font=('Poppins', 9), command=lambda: handle_view_task(updatename_entry.get().lower(), updatetask_text))
    viewtask_btn.grid(row=2, column=1,padx=10, pady=10)  #Lambda is used to pass arguments.

    newtaskdescription_label = tk.Label(frame, text = "New task description : ", font = (("Poppins)", 16)))
    newtaskdescription_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    newtaskdescription_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    newtaskdescription_entry.grid(row=3, column=1, padx=10, pady=10)

    newtaskpriority_label = tk.Label(frame, text = "New task priority : ", font = (("Poppins)", 16)))
    newtaskpriority_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    newtaskpriority_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    newtaskpriority_entry.grid(row=4, column=1, padx=10, pady=10)

    newtaskduedate_label = tk.Label(frame, text = "New task due date : ", font = (("Poppins)", 16)))
    newtaskduedate_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    newtaskduedate_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    newtaskduedate_entry.grid(row=5, column=1, padx=10, pady=10)

    update_btn = tk.Button(frame, text="Update", command=lambda: handle_update(updatename_entry.get().lower(), newtaskdescription_entry.get(), newtaskpriority_entry.get(), newtaskduedate_entry.get()), width=20, font=('Poppins', 16))
    update_btn.grid(row=6, column=1,padx=10, pady=10)
    backtoMenu_btn = tk.Button(frame, text = "Back to Menu",command=main_menu, width=20, font=('Poppins', 16))
    backtoMenu_btn.grid(row = 6, column=0,padx=10, pady=10)
    frame.pack(padx=10, pady=10)

    def handle_update(task_name, new_description, new_priority, new_due_date):
        tasks[task_name]['description'] = new_description
        tasks[task_name]['priority'] = new_priority
        if new_priority.lower() not in ["high", "medium", "low"]:
            messagebox.showerror("Error", "Invalid priority. Must be high/medium/low")
            return

        tasks[task_name]['due_date'] = new_due_date
        save_tasks()
        messagebox.showinfo("Success", "Task updated successfully")
        updateTask()


def deleteTask():
    clear_frame()
    window.geometry("700x500")
    label = tk.Label(window, text="Delete a Task", font=('Poppins', 25))
    label.pack(pady=10)

    frame = tk.Frame(window)
    deletetaskname_label = tk.Label(frame, text = "Task name : ", font = (("Poppins)", 16)))
    deletetaskname_label.grid(row=0, column=0, padx=10, pady=10)

    deletetaskname_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    deletetaskname_entry.grid(row=0, column=1, padx=10, pady=10)

    viewtask_text = tk.Text(frame,width=45, height=8, font = (("Poppins)", 16)))
    viewtask_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    viewtask_btn = tk.Button(frame, text="Find Task", width=10, font=('Poppins', 9), command=lambda: handle_view_task(deletetaskname_entry.get().lower(), viewtask_text))
    viewtask_btn.grid(row=2, column=1,padx=10, pady=10)  #Lambda is used to pass arguments.

    delete_btn = tk.Button(frame, text="Delete", command=lambda: handle_delete(deletetaskname_entry.get()), width=20, font=('Poppins', 16))
    delete_btn.grid(row=3, column=1,padx=10, pady=10)

    backtoMenu_btn = tk.Button(frame, text = "Back to Menu",command=main_menu, width=20, font=('Poppins', 16))
    backtoMenu_btn.grid(row=3, column=0, padx=10, pady=10)
    frame.pack()

    def handle_delete(task_name):
        del tasks[task_name]
        save_tasks()
        messagebox.showinfo("Success", "Task deleted successfully")
        deleteTask()


def main_menu():
    clear_frame()
    label = tk.Label(window, text="Main Menu", font=('Poppins', 25))
    label.pack(pady=10)

    addTask_btn = tk.Button(window, text = "Add a Task",command=addTask, width=20, font=('Poppins', 16))
    addTask_btn.pack(pady=10)

    viewTask_btn = tk.Button(window, text = "View a Task",command=viewTask, width=20, font=('Poppins', 16))
    viewTask_btn.pack(pady=10)

    updateTask_btn = tk.Button(window, text = "Update a Task",command=updateTask, width=20, font=('Poppins', 16))
    updateTask_btn.pack(pady=10)

    deleteTask_btn = tk.Button(window, text = "Delete a Task",command=deleteTask, width=20, font=('Poppins', 16))
    deleteTask_btn.pack(pady=10)
def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()

load_tasks()

window = tk.Tk()
window.geometry("700x500")
window.title("Stage 4")
main_menu()
window.mainloop()



# Error handling park eka :

#     in add task when add is clicked, must display "All fields should be filled"

#     in add task, input should be cleared after clicking addTask

#     in update task, when user click update without any input, its should display "All fields should be filled"

#     Task name input capital or simple error ////DONE

