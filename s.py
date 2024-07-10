import tkinter as tk
from tkinter import messagebox

# Correct password for validation
correct_password = "123"

# Function to open the success window
def open_success_window(db_name):
    success_window = tk.Tk()
    success_window.title("Success")

    label_success = tk.Label(success_window, text=f"Database: {db_name}\nLogin Successful!")
    label_success.pack(pady=20)

    button_close = tk.Button(success_window, text="Close", command=success_window.destroy)
    button_close.pack(pady=10)

    success_window.mainloop()

# Function to validate credentials and open success window if correct
def validate_credentials(db_name, password):
    if password == correct_password:
        messagebox.showinfo("Success", "Login Successful!")
        root.destroy()
        open_success_window(db_name)
    else:
        messagebox.showerror("Error", "Incorrect password")

# Function to get the database name and password from the first window
def get_db_credentials():
    db_name = entry_db_name.get()
    password = entry_password.get()
    if db_name and password:
        validate_credentials(db_name, password)
    else:
        messagebox.showwarning("Input Error", "Please enter both database name and password")

# First window to enter database name and password
root = tk.Tk()
root.title("Database Login")

label_db_name = tk.Label(root, text="Enter Database Name:")
label_db_name.pack(pady=10)

entry_db_name = tk.Entry(root)
entry_db_name.pack(pady=10)

label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=10)

button_submit = tk.Button(root, text="Submit", command=get_db_credentials)
button_submit.pack(pady=10)

root.mainloop()
