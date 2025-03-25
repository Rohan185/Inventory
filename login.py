import tkinter as tk
from tkinter import messagebox, StringVar
import sqlite3
import os

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System | Developed by Parag & Omkrish")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.EmployeeID = StringVar()
        self.password = StringVar()

        # UI Elements
        tk.Label(root, text="Employee ID", font=("Arial", 14)).pack(pady=10)
        self.eid_entry = tk.Entry(root, textvariable=self.EmployeeID, font=("Arial", 14))
        self.eid_entry.pack(pady=5)

        tk.Label(root, text="Password", font=("Arial", 14)).pack(pady=10)
        self.pass_entry = tk.Entry(root, textvariable=self.password, show="*", font=("Arial", 14))
        self.pass_entry.pack(pady=5)

        tk.Button(root, text="Login", command=self.login, font=("Arial", 14), bg="blue", fg="white").pack(pady=20)

    def login(self):
        """Handles user login and redirects to dashboard."""
        with sqlite3.connect('ims.db') as con:
            cur = con.cursor()
            cur.execute("SELECT utype FROM Employee WHERE eid=? AND pass=?", (self.EmployeeID.get(), self.password.get()))
            user = cur.fetchone()

        if user is None:
            messagebox.showerror('Error', 'Invalid Username or Password', parent=self.root)
        else:
            self.root.destroy()
            os.system("python dashboard.py" if os.path.exists("dashboard.py") else "echo 'dashboard.py not found'")

if __name__ == "__main__":
    root = tk.Tk()
    obj = LoginSystem(root)
    root.mainloop()
