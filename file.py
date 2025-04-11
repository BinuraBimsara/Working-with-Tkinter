import tkinter as tk

window = tk.Tk()
window.geometry("600x600")
window.title("Test GUI")

label = tk.Label(window, text = "Hello World!", font = ('Poppins',25))
label.pack(padx=20 , pady=20)

frame = tk.Frame(window)

# textbox = tk.Text(window, height=1, font = ('Poppins',16))
# textbox.pack(padx=10)

# entry = tk.Entry(window, font = ('Poppins',16))
# entry.pack()

# button = tk.Button(window, text="Click ME", font = ('Poppins',16))
# button.pack(pady=10)

label1 = tk.Label(frame, text = "Hello World!", font = ('Poppins',25))
label1.grid(row=0, column=0, padx=10, pady= 10)

entry1 = tk.Entry(frame, font = ('Poppins',16))
entry1.grid(row=0, column=1 )

label2 = tk.Label(frame, text = "Hello World!", font = ('Poppins',25))
label2.grid(row=1, column=0, padx=10, pady= 10)

entry2 = tk.Entry(frame, font = ('Poppins',16))
entry2.grid(row=1, column=1 )

frame.pack(fill='x')



window.mainloop()