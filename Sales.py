from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
from Billing import BILLINGCLASS

class Salesclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1110x500+220+130")
        self.root.title("Inventory Management System | Developed by Parag & Omkrish")
        self.root.config(bg="white")
        
        # Title
        title = Label(self.root, text="Sales Management", font=("goudy old style", 30),
                     bg="#184a45", fg="white", bd=3, relief=RIDGE)
        title.pack(side=TOP, fill=X, padx=10, pady=2)

        # Sales Frame
        sales_frame = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        sales_frame.place(x=10, y=60, width=1090, height=430)

        # Left Frame - Customer Details
        customer_frame = LabelFrame(sales_frame, text="Customer Details", font=("goudy old style", 15, "bold"),
                                  bg="white", bd=2)
        customer_frame.place(x=10, y=10, width=350, height=140)

        # Customer Name
        lbl_name = Label(customer_frame, text="Name", font=("times new roman", 15), bg="white")
        lbl_name.place(x=10, y=20)
        self.txt_name = Entry(customer_frame, font=("times new roman", 13), bg="lightyellow")
        self.txt_name.place(x=90, y=20, width=200)

        # Contact
        lbl_contact = Label(customer_frame, text="Contact", font=("times new roman", 15), bg="white")
        lbl_contact.place(x=10, y=60)
        self.txt_contact = Entry(customer_frame, font=("times new roman", 13), bg="lightyellow")
        self.txt_contact.place(x=90, y=60, width=200)

        # Right Frame - Product Details
        product_frame = LabelFrame(sales_frame, text="Product Details", font=("goudy old style", 15, "bold"),
                                 bg="white", bd=2)
        product_frame.place(x=370, y=10, width=700, height=400)

        # Product Search
        lbl_search = Label(product_frame, text="Search Product | By Name", 
                          font=("times new roman", 15), bg="white")
        lbl_search.place(x=10, y=20)
        self.txt_search = Entry(product_frame, font=("times new roman", 13), bg="lightyellow")
        self.txt_search.place(x=220, y=20, width=200)
        
        # Search Button
        btn_search = Button(product_frame, text="Search", font=("goudy old style", 15),
                          bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=440, y=18, width=120, height=30)

        # Product Table Frame
        table_frame = Frame(product_frame, bd=3, relief=RIDGE)
        table_frame.place(x=10, y=70, width=670, height=280)

        scrolly = Scrollbar(table_frame, orient=VERTICAL)
        scrollx = Scrollbar(table_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(table_frame, columns=("pid", "name", "price", "qty", "status"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="PID")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Qty")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=60)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=70)
        self.product_table.column("qty", width=60)
        self.product_table.column("status", width=80)
        self.product_table.pack(fill=BOTH, expand=1)

        # Buttons Frame
        btn_frame = Frame(sales_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=10, y=160, width=350, height=250)

        btn_new_bill = Button(btn_frame, text="New Bill", font=("goudy old style", 15, "bold"),
                            bg="#2196f3", fg="white", cursor="hand2", command=self.new_bill)
        btn_new_bill.place(x=10, y=20, width=330, height=50)

        btn_clear = Button(btn_frame, text="Clear", font=("goudy old style", 15, "bold"),
                          bg="#607d8b", fg="white", cursor="hand2", command=self.clear)
        btn_clear.place(x=10, y=80, width=330, height=50)

        # Show all products initially
        self.show()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT pid, name, price, qty, status FROM Product WHERE status='Active'")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def new_bill(self):
        self.new_win = Toplevel(self.root)
        self.new_bill = BILLINGCLASS(self.new_win)

    def clear(self):
        self.txt_name.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_search.delete(0, END)
        self.show()

if __name__ == "__main__":
    root = Tk()
    obj = Salesclass(root)
    root.mainloop() 