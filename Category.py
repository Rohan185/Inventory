from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os

class CategoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1110x500+220+130")
        self.root.title("Inventory Management System | Developed by Parag  & Omkrish")
        self.root.config(bg="white")
        self.root.protocol("WM_DELETE_WINDOW", self.open_dashboard)  # When window is closed, open dashboard

        # Variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()

        # Title
        Label(self.root, text="Manage Product Category", font=("goudy old style", 30),
              bg="#184a45", fg="White", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=2)

        # Category Frame
        category_frame = Frame(self.root, bg="white")
        category_frame.place(x=50, y=100, width=300, height=200)

        Label(category_frame, text="Enter Category Name", font=("goudy old style", 18), bg="white").place(x=10, y=10)
        Entry(category_frame, textvariable=self.var_name, font=("goudy old style", 18), bg="lightyellow").place(x=10, y=50, width=250)

        Button(category_frame, text="Add", command=self.add, font=("goudy old style", 18),
               bg="#4caf50", fg="white", cursor="hand2").place(x=10, y=100, width=100, height=30)
        Button(category_frame, text="Delete", command=self.delete, font=("goudy old style", 18),
               bg="red", fg="white", cursor="hand2").place(x=120, y=100, width=100, height=30)

        # Category Details
        category_details_frame = Frame(self.root, bd=3, relief=RIDGE)
        category_details_frame.place(x=700, y=100, width=380, height=300)

        self.category_details_treeview = ttk.Treeview(category_details_frame, columns=("cid", "name"), selectmode=BROWSE)
        self.category_details_treeview.heading("cid", text="C ID")
        self.category_details_treeview.heading("name", text="Name")
        self.category_details_treeview["show"] = "headings"
        self.category_details_treeview.column("cid", width=90)
        self.category_details_treeview.column("name", width=100)
        self.category_details_treeview.pack(fill=BOTH, expand=1)
        self.category_details_treeview.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def add(self):
        """Add a new category."""
        with sqlite3.connect('ims.db') as con:
            cur = con.cursor()
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name required", parent=self.root)
                return
            cur.execute("SELECT * FROM Category WHERE name=?", (self.var_name.get(),))
            if cur.fetchone():
                messagebox.showerror("Error", "Category already exists", parent=self.root)
            else:
                cur.execute("INSERT INTO Category(name) VALUES(?)", (self.var_name.get(),))
                con.commit()
                messagebox.showinfo("Success", "Category added successfully", parent=self.root)
                self.show()

    def show(self):
        """Display all categories in the table."""
        with sqlite3.connect('ims.db') as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM Category")
            rows = cur.fetchall()
            self.category_details_treeview.delete(*self.category_details_treeview.get_children())
            for row in rows:
                self.category_details_treeview.insert('', END, values=row)

    def get_data(self, ev):
        """Retrieve selected category data."""
        f = self.category_details_treeview.focus()
        content = self.category_details_treeview.item(f)
        row = content.get('values', [])
        if row:
            self.var_cat_id.set(row[0])
            self.var_name.set(row[1])

    def delete(self):
        """Delete a selected category."""
        with sqlite3.connect('ims.db') as con:
            cur = con.cursor()
            if not self.var_cat_id.get():
                messagebox.showerror("Error", "Please select a category", parent=self.root)
                return
            cur.execute("SELECT * FROM Category WHERE cid=?", (self.var_cat_id.get(),))
            if not cur.fetchone():
                messagebox.showerror("Error", "Category not found", parent=self.root)
            else:
                if messagebox.askyesno("Confirm", "Do you want to delete this category?", parent=self.root):
                    cur.execute("DELETE FROM Category WHERE cid=?", (self.var_cat_id.get(),))
                    con.commit()
                    messagebox.showinfo("Deleted", "Category deleted successfully", parent=self.root)
                    self.show()
                    self.var_cat_id.set("")
                    self.var_name.set("")

    def open_dashboard(self):
        """Open dashboard.py when category window is closed."""
        self.root.destroy()
        os.system("python dashboard.py" if os.path.exists("dashboard.py") else "echo 'dashboard.py not found'")

if __name__ == "__main__":
    root = Tk()
    obj = CategoryClass(root)
    root.mainloop()
