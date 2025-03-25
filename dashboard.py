from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import os
import time

# Import classes with error handling
try:
    from Employee import EmployeeClass
    from Supplier import Supplierclass
    from Category import CategoryClass
    from Product import Productclass
    from Sales import Salesclass
except ImportError as e:
    print(f"Error importing module: {e}")
    EmployeeClass = None
    Supplierclass = None
    CategoryClass = None
    Productclass = None
    Salesclass = None

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Developed by Parag")
        self.root.config(bg="white")

        # Initialize database connection
        self.conn = sqlite3.connect('ims.db')
        self.cursor = self.conn.cursor()

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Title bar
        self.icon_title = PhotoImage(file="logo.png") if os.path.exists("logo.png") else None
        title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout button
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2", command=self.logout)
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # Clock Label
        self.lbl_clock = Label(self.root, text="Welcome to IMS System", font=("times new roman", 15),
                               bg="#4d636d", fg="white", anchor="w")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # Left menu
        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=102, width=200, height=565)

        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP, fill=X)

        menu_items = [
            ("Employee", self.employee),
            ("Supplier", self.supplier),
            ("Category", self.category),
            ("Product", self.product),
            ("Sales", self.sales),
            ("Exit", self.root.quit)
        ]

        for text, cmd in menu_items:
            Button(LeftMenu, text=text, command=cmd, font=("times new roman", 20, "bold"), bg="white",
                   bd=3, cursor="hand2").pack(side=TOP, fill=X)

        # Dashboard summary
        self.stat_labels = {}
        stats = ["Employee", "Supplier", "Category", "Product", "Sales"]
        colors = ["#33bbf9", "#ff5722", "#009688", "#607d8b", "#ffc107"]
        
        for i, stat in enumerate(stats):
            self.stat_labels[stat] = Label(self.root, text=f"Total {stat}\n[0]", bd=5, relief=RIDGE, bg=colors[i],
                                           fg="white", font=("goudy old style", 20, "bold"))
            self.stat_labels[stat].place(x=300 + (i % 2) * 350, y=120 + (i // 2) * 180, height=150, width=300)

        # Footer
        Label(self.root, text="IMS Inventory Management System | Developed by Parag & Omkrish",
              font=("times new roman", 15), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)

        self.update_content()

    def update_content(self):
        try:
            self.cursor.execute("SELECT COUNT(*) FROM Employee")
            self.stat_labels["Employee"].config(text=f"Total Employee\n[{self.cursor.fetchone()[0]}]")

            self.cursor.execute("SELECT COUNT(*) FROM Supplier")
            self.stat_labels["Supplier"].config(text=f"Total Supplier\n[{self.cursor.fetchone()[0]}]")

            self.cursor.execute("SELECT COUNT(*) FROM Category")
            self.stat_labels["Category"].config(text=f"Total Category\n[{self.cursor.fetchone()[0]}]")

            self.cursor.execute("SELECT COUNT(*) FROM Product")
            self.stat_labels["Product"].config(text=f"Total Product\n[{self.cursor.fetchone()[0]}]")

            self.stat_labels["Sales"].config(text=f"Total Sales\n[{len(os.listdir('bill')) if os.path.exists('bill') else 0}]")

            time_now = time.strftime("%I:%M:%S %p")
            date_now = time.strftime("%d/%m/%Y")
            self.lbl_clock.config(text=f"Date: {date_now}\t Time: {time_now}")
            self.lbl_clock.after(1000, self.update_content)
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py" if os.path.exists("login.py") else "echo 'Login script not found'")

    def employee(self):
        if EmployeeClass:
            self.new_win = Toplevel(self.root)
            EmployeeClass(self.new_win)
        else:
            messagebox.showerror("Error", "Employee module not found", parent=self.root)

    def supplier(self):
        if Supplierclass:
            self.new_win = Toplevel(self.root)
            Supplierclass(self.new_win)

    def category(self):
        if CategoryClass:
            self.new_win = Toplevel(self.root)
            CategoryClass(self.new_win)

    def product(self):
        if Productclass:
            self.new_win = Toplevel(self.root)
            Productclass(self.new_win)

    def sales(self):
        if Salesclass:
            self.new_win = Toplevel(self.root)
            Salesclass(self.new_win)

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
