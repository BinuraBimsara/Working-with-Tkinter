import tkinter as tk

window = tk.Tk()
window.geometry("700x500")
window.title("Stage 4")

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

    frame.pack(padx=10, pady=10)

    submit_btn = tk.Button(window, text="Submit", width=20, font=('Poppins', 16))
    submit_btn.pack(pady=10)
    backtoMenu_btn = tk.Button(window, text = "Back to Menu",command=main_menu, width=20, font=('Poppins', 16))
    backtoMenu_btn.pack(pady=10)

def viewTask():
    clear_frame()
    window.geometry("700x500")
    label = tk.Label(window, text="View a Task", font=('Poppins', 25))
    label.pack(pady=10)

    frame = tk.Frame(window)
    taskname_label = tk.Label(frame, text = "Task name : ", font = (("Poppins)", 16)))
    taskname_label.grid(row=0, column=0, padx=10, pady=10)

    taskname_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    taskname_entry.grid(row=0, column=1, padx=10, pady=10)
    frame.pack()

    viewtask_text = tk.Text(window, height=8, font = (("Poppins)", 16)))
    viewtask_text.pack(padx=10, pady=10)

    backtoMenu_btn = tk.Button(window, text = "Back to Menu",command=main_menu, width=20, font=('Poppins', 16))
    backtoMenu_btn.pack(pady=10)


def updateTask():
    clear_frame()
    window.geometry("700x650")
    label = tk.Label(window, text="Update a Task", font=('Poppins', 25))
    label.pack(pady=10)

    frame = tk.Frame(window)

    updatename_label = tk.Label(frame, text="Task name : ", font = (("Poppins)", 16)))
    updatename_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    updatename_Entry = tk.Entry(frame, font = (("Poppins)", 16)))
    updatename_Entry.grid(row=0, column=1, padx=10, pady=10)

    updatetask_text = tk.Text(frame,width=45, height=8, font = (("Poppins)", 16)))
    updatetask_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    newtaskdescription_label = tk.Label(frame, text = "New task description : ", font = (("Poppins)", 16)))
    newtaskdescription_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
    newtaskdescription_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    newtaskdescription_entry.grid(row=2, column=1, padx=10, pady=10)

    newtaskpriority_label = tk.Label(frame, text = "New task priority : ", font = (("Poppins)", 16)))
    newtaskpriority_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    newtaskpriority_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    newtaskpriority_entry.grid(row=3, column=1, padx=10, pady=10)

    newtaskduedate_label = tk.Label(frame, text = "New task due date : ", font = (("Poppins)", 16)))
    newtaskduedate_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    newtaskduedate_entry = tk.Entry(frame, font = (("Poppins)", 16)))
    newtaskduedate_entry.grid(row=4, column=1, padx=10, pady=10)

    update_btn = tk.Button(frame, text="Update", width=20, font=('Poppins', 16))
    update_btn.grid(row=5, column=1,padx=10, pady=10)
    backtoMenu_btn = tk.Button(frame, text = "Back to Menu",command=main_menu, width=20, font=('Poppins', 16))
    backtoMenu_btn.grid(row = 5, column=0,padx=10, pady=10)

    frame.pack(padx=10, pady=10)
def deleteTask():
    clear_frame()
    window.geometry("700x500")
    label = tk.Label(window, text="Delete a Task", font=('Poppins', 25))
    backtoMenu_btn = tk.Button(window, text = "Back to Menu",command=main_menu, width=20, font=('Poppins', 16))
    label.pack(pady=10)
    backtoMenu_btn.pack(pady=10)

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



main_menu()
window.mainloop()