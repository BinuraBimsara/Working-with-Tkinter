import tkinter as tk

def show_main_menu():
    clear_frame()
    root.geometry("500x300")
    tk.Label(main_frame, text="Main Menu", font=("Arial", 16)).pack(pady=10)
    tk.Button(main_frame, text="Add", width=20, command=show_add).pack(pady=5)
    tk.Button(main_frame, text="Update", width=20, command=show_update).pack(pady=5)
    tk.Button(main_frame, text="Delete", width=20, command=show_delete).pack(pady=5)

def show_add():
    clear_frame()
    root.geometry("800x800")
    tk.Label(main_frame, text="Add Section", font=("Arial", 14)).pack(pady=10)
    tk.Button(main_frame, text="Run Add", command=add).pack(pady=5)
    tk.Button(main_frame, text="Back to Menu", command=show_main_menu).pack(pady=20)

def show_update():
    clear_frame()
    root.geometry("800x800")
    tk.Label(main_frame, text="Update Section", font=("Arial", 14)).pack(pady=10)
    tk.Button(main_frame, text="Run Update", command=update).pack(pady=5)
    tk.Button(main_frame, text="Back to Menu", command=show_main_menu).pack(pady=20)

def show_delete():
    root.geometry("800x800")
    clear_frame()
    tk.Label(main_frame, text="Delete Section", font=("Arial", 14)).pack(pady=10)
    tk.Button(main_frame, text="Run Delete", command=delete).pack(pady=5)
    tk.Button(main_frame, text="Back to Menu", command=show_main_menu).pack(pady=20)

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def add():
    print("Add logic")

def update():
    print("Update logic")

def delete():
    print("Delete logic")

# Main GUI setup
root = tk.Tk()
root.title("Main Menu Navigation Example")
root.geometry("400x300")

main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Load main menu initially
show_main_menu()

root.mainloop()
