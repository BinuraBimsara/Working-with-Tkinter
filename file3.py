import tkinter as tk

# Dictionary to store data
data_dict = {}

# Main logic functions
def add():
    name = name_entry.get()
    age = age_entry.get()
    priority = priority_entry.get()
    duedate = duedate_entry.get()

    if name and age and priority and duedate:
        data_dict[name] = age
        print("Current Data:", data_dict)
        name_entry.delete(0, tk.END)
        age_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        duedate_entry.delete(0, tk.END)
        status_label.config(text="Data saved!", fg="green")
    else:
        status_label.config(text="Please enter all details.", fg="red")

def update():
    print("Update logic here")

def delete():
    print("Delete logic here")

# GUI handlers
def show_main_menu():
    root.geometry("400x300")
    clear_frame()
    tk.Label(main_frame, text="Main Menu", font=("Poppins", 18)).pack(pady=10)
    tk.Button(main_frame, text="Add", width=20, command=show_add, font='Poppins').pack(pady=5)
    tk.Button(main_frame, text="Update", width=20, command=show_update, font='Poppins').pack(pady=5)
    tk.Button(main_frame, text="Delete", width=20, command=show_delete, font='Poppins').pack(pady=5)

def show_add():
    root.geometry("600x400")
    clear_frame()

    tk.Label(main_frame, text="Add a Task", font=("Poppins", 18)).pack(pady=10)

    tk.Label(main_frame, text="Task name:").pack()
    global name_entry
    name_entry = tk.Entry(main_frame)
    name_entry.pack(pady=5)

    tk.Label(main_frame, text="Task description:").pack()
    global age_entry
    age_entry = tk.Entry(main_frame)
    age_entry.pack(pady=5)

    tk.Label(main_frame, text="Task proiority:").pack()
    global priority_entry
    priority_entry = tk.Entry(main_frame)
    priority_entry.pack(pady=5)

    tk.Label(main_frame, text="Task due date:").pack()
    global duedate_entry
    duedate_entry = tk.Entry(main_frame)
    duedate_entry.pack(pady=5)


    tk.Button(main_frame, text="Submit", command=add).pack(pady=10)

    global status_label
    status_label = tk.Label(main_frame, text="", fg="green")
    status_label.pack()

    tk.Button(main_frame, text="Back to Menu", command=show_main_menu).pack(pady=10)

def show_update():
    root.geometry("600x400")
    clear_frame()
    tk.Label(main_frame, text="Update a Task", font=("Poppins", 18)).pack(pady=10)
    tk.Button(main_frame, text="Run Update", command=update).pack(pady=5)
    tk.Button(main_frame, text="Back to Menu", command=show_main_menu).pack(pady=20)

def show_delete():
    root.geometry("400x200")
    clear_frame()
    tk.Label(main_frame, text="Delete a Task", font=("Poppins", 18)).pack(pady=10)
    tk.Button(main_frame, text="Run Delete", command=delete).pack(pady=5)
    tk.Button(main_frame, text="Back to Menu", command=show_main_menu).pack(pady=20)

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

# Main GUI setup
root = tk.Tk()
root.title("Menu-Driven GUI with Input")
root.geometry("600x400")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Show main menu on startup
show_main_menu()

root.mainloop()
