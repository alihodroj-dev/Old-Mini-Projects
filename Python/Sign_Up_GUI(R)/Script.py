# imports
import tkinter as gui

# Functions
def login_func():
    filer = open("Accs.txt", "r")
    inputs = []
    for acc in filer.readlines():
        inputs.append(acc)
    filew = open("Accs.txt", "w")
    for x in inputs:
        filew.write(x)
    inputs = []
    inputs.append(email_entry.get())
    inputs.append(password_entry.get())
    for y in inputs:
        filew.write("\n" + y)
    email_entry.destroy()
    password_entry.destroy()

# Variables
root_window = gui.Tk()
root_window.title("Toxic Code")
root_window.geometry("400x400")
root_window.resizable(False, False)
root_window.configure(background="green")
root_window.grid_columnconfigure(0, weight=1)

heading_title = gui.Label(root_window, text="Sign Up", fg="black", font=("Sans-serif", 30), background="green")
heading_title.grid(row=0, column=0, sticky="N", pady=30)

email_title = gui.Label(root_window, text="Email", fg="black", font=("Sans-serif", 12), background="green")
email_title.grid(row=1, column=0, pady=20)

email_entry = gui.Entry(width=50)
email_entry.grid(row=2, column=0)

password_title = gui.Label(root_window, text="Password", fg="black", font=("Sans-serif", 12), background="green")
password_title.grid(row=3, column=0, pady=20)

password_entry = gui.Entry(width=50)
password_entry.grid(row=4, column=0)

submit_btn = gui.Button(text="Submit", command=login_func)
submit_btn.grid(row=5, column=0, pady=30)

# firing
if __name__ == "__main__":
    root_window.mainloop()