from math import cos
from tkinter import *
from PIL import Image, ImageTk #pip install pillow
from tkinter import ttk, messagebox
import sqlite3
import time
import os
import tempfile


class BILLINGCLASS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")  # Corrected
        self.root.title("Inventory Management System | Developed by Parag & Omkrish")  # Corrected
        self.root.config(bg="white")
        self.cart_list=[]
        self.chk_print=0

        # Variables
        self.var_pid = StringVar()
        self.var_pname = StringVar()
        self.var_Price = StringVar()
        self.var_Qty = StringVar()
        self.var_Stock = StringVar()
        self.var_cal_input = StringVar()
        self.var_Search = StringVar()
        self.var_cname = StringVar()
        self.var_contact = StringVar()

        # ===title====
        try:
            self.icon_title = PhotoImage(file="images/logo.png")
            title = Label(self.root, text="Inventory Management System", image=self.icon_title, compound=LEFT,
                        font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        except:
            # If logo not found, create label without image
            title = Label(self.root, text="Inventory Management System",
                        font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)
        #===btn_logout====
        Btn_logout=Button(self.root,command=self.logout,text="Logout",font=("times new roman",15,"bold"),bg="Yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #===clock====
        self.lal_clock= Label(self.root, text="Welcome to Inventory Management System\t\t Date:DD/MM.YYYY\t\t Time:HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white")
        self.lal_clock.place(x=0, y=70, relwidth=1, height=30)

        #====Product===========================================================
        
        # Product Frame
        self.ProductFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        self.ProductFrame1.place(x=6, y=110, width=410, height=550)
        
        ptitle = Label(self.ProductFrame1, text="All Products", font=("goudy old style", 20, "bold"),
                      bg="#262626", fg="white")
        ptitle.pack(side=TOP, fill=X)
        
        # Product Search
        self.ProductFrame2 = Frame(self.ProductFrame1, bd=4, relief=RIDGE, bg="white")
        self.ProductFrame2.place(x=2, y=42, width=398, height=90)

        lbl_search = Label(self.ProductFrame2, text="Search Product | by Name",
                         font=("times new roman", 15, "bold"), bg="white", fg="green")
        lbl_search.place(x=2, y=5)

        txt_search = Entry(self.ProductFrame2, textvariable=self.var_Search,
                         font=("times new roman", 15), bg="lightyellow")
        txt_search.place(x=128, y=7, width=150, height=22)

        btn_search = Button(self.ProductFrame2, text="Search", command=self.search,
                          font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_search.place(x=285, y=5, width=100, height=25)

        btn_show_all = Button(self.ProductFrame2, text="Show All", command=self.show,
                            font=("goudy old style", 15), bg="#83b531", fg="white", cursor="hand2")
        btn_show_all.place(x=285, y=45, width=100, height=25)

        #===Product Frame Details===================================================

        # Product Details Frame
        product_frame = Frame(self.ProductFrame1, bd=3, relief=RIDGE)
        product_frame.place(x=2, y=140, width=398, height=375)

        scrolly = Scrollbar(product_frame, orient=VERTICAL)
        scrollx = Scrollbar(product_frame, orient=HORIZONTAL)

        self.product_Table = ttk.Treeview(product_frame, columns=("pid", "name", "price", "qty", "status"),
                                        yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid", text="PID")
        self.product_Table.heading("name", text="Name")
        self.product_Table.heading("price", text="Price")
        self.product_Table.heading("qty", text="Qty")
        self.product_Table.heading("status", text="Status")
        self.product_Table["show"] = "headings"

        self.product_Table.column("pid", width=40)
        self.product_Table.column("name", width=100)
        self.product_Table.column("price", width=100)
        self.product_Table.column("qty", width=40)
        self.product_Table.column("status", width=90)

        self.product_Table.pack(fill=BOTH, expand=1)
        self.product_Table.bind("<ButtonRelease-1>", self.get_data)

        lbl_note = Label(self.ProductFrame1, text="Note: Enter 0 Qty to remove Product from the Cart",
                        font=("goudy old style", 12), anchor="w", bg="white", fg="red")
        lbl_note.pack(side=BOTTOM, fill=X)

        #=====Customer Frame=========================================================================================================================================================
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        ctitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",20),bg="lightgray").pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white",fg="green").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightyellow").place(x=80,y=35,width=180)

        lbl_Contact=Label(CustomerFrame,text="Contact No",font=("times new roman",15),bg="white",fg="green").place(x=270,y=35)
        txt_Contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightyellow").place(x=380,y=35,width=140)
       #====Cal Cart Frame====================================================
        Cal_Cart_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
       
       #====Calculator Frame=============================================
        self.var_Cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_Cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text='7',font=('arial',15,"bold"),command=lambda:self.get_input('7'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,"bold"),command=lambda:self.get_input('8'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,"bold"),command=lambda:self.get_input('9'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,"bold"),command=lambda:self.get_input('+'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,column=3)

        btn_4=Button(Cal_Frame,text='4',font=('arial',15,"bold"),command=lambda:self.get_input('4'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,"bold"),command=lambda:self.get_input('5'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,"bold"),command=lambda:self.get_input('6'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_minus=Button(Cal_Frame,text='-',font=('arial',15,"bold"),command=lambda:self.get_input('-'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,column=3)

        btn_1=Button(Cal_Frame,text='1',font=('arial',15,"bold"),command=lambda:self.get_input('1'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,"bold"),command=lambda:self.get_input('2'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,"bold"),command=lambda:self.get_input('3'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,"bold"),command=lambda:self.get_input('*'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text='0',font=('arial',15,"bold"),command=lambda:self.get_input('0'),bd=5,width=5,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,"bold"),command=self.clear_cal,bd=5,width=5,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,"bold"),command=self.perform_cal,bd=5,width=5,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,"bold"),command=lambda:self.get_input('/'),bd=5,width=5,pady=15,cursor="hand2").grid(row=4,column=3)

     #=====cart frame========================================== 
        cart_frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        self.cartTitle=Label(cart_frame,text="Cart\t Total Product:[0]",font=("goudy old style",15,"bold"),bg="#262626",fg="white")
        self.cartTitle.pack(side=TOP,fill=X)


        Scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        Scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.Cart_Table=ttk.Treeview(cart_frame,columns=("pid","name","price","qty"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.Cart_Table.xview)
        Scrolly.config(command=self.Cart_Table.yview)

        self.Cart_Table.heading("pid",text="Pid")
        self.Cart_Table.heading("name",text="Name")
        self.Cart_Table.heading("price",text="Price")
        self.Cart_Table.heading("qty",text="Qty")
        self.Cart_Table["show"]="headings"
        
        self.Cart_Table.column("pid",width=40)
        self.Cart_Table.column("name",width=100)
        self.Cart_Table.column("price",width=90)
        self.Cart_Table.column("qty",width=40)
        self.Cart_Table.pack(fill=BOTH,expand=1)
        self.Cart_Table.bind("<ButtonRelease-1>",self.get_data_cart)

   #=====Add Cart widgets Frame==================================
        self.Add_CartwidgetsFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        self.Add_CartwidgetsFrame.place(x=420, y=550, width=520, height=110)

        lbl_p_name = Label(self.Add_CartwidgetsFrame, text="Product Name", font=("times new roman", 15), bg="white")
        lbl_p_name.place(x=5, y=5)

        txt_p_name = Entry(self.Add_CartwidgetsFrame, textvariable=self.var_pname, 
                          font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_p_name.place(x=5, y=35, width=190, height=22)

        lbl_p_price = Label(self.Add_CartwidgetsFrame, text="Price per Qty", font=("times new roman", 15), bg="white")
        lbl_p_price.place(x=230, y=5)

        txt_p_price = Entry(self.Add_CartwidgetsFrame, textvariable=self.var_Price, 
                           font=("times new roman", 15), bg="lightyellow", state="readonly")
        txt_p_price.place(x=230, y=35, width=150, height=22)

        lbl_p_qty = Label(self.Add_CartwidgetsFrame, text="Quantity", font=("times new roman", 15), bg="white")
        lbl_p_qty.place(x=390, y=5)

        txt_p_qty = Entry(self.Add_CartwidgetsFrame, textvariable=self.var_Qty, 
                         font=("times new roman", 15), bg="lightyellow")
        txt_p_qty.place(x=390, y=35, width=120, height=22)

        self.lbl_inStock = Label(self.Add_CartwidgetsFrame, text="In Stock", font=("times new roman", 15), bg="white")
        self.lbl_inStock.place(x=5, y=70)

        btn_clear_cart = Button(self.Add_CartwidgetsFrame, text="Clear", command=self.clear_cart,
                              font=("times new roman", 15, "bold"), bg="lightgray", cursor="hand2")
        btn_clear_cart.place(x=180, y=70, width=150, height=30)

        btn_add_cart = Button(self.Add_CartwidgetsFrame, text="Add | Update Cart", command=self.add_update_cart,
                            font=("times new roman", 15, "bold"), bg="orange", cursor="hand2")
        btn_add_cart.place(x=340, y=70, width=180, height=30)

  #===========Billing Area==========================================================================================
        # Billing Area
        self.billFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.billFrame.place(x=953, y=110, width=410, height=410)

        self.bill_title = Label(self.billFrame, text="Customer Bill Area", 
                              font=("goudy old style", 20, "bold"), bg="#262626", fg="white")
        self.bill_title.pack(side=TOP, fill=X)
        
        scrolly = Scrollbar(self.billFrame, orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)

        self.txt_bill_area = Text(self.billFrame, yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH, expand=1)
        scrolly.config(command=self.txt_bill_area.yview)

        # Billing Buttons
        self.billMenuFrame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.billMenuFrame.place(x=953, y=520, width=410, height=140)

        self.lbl_amnt = Label(self.billMenuFrame, text="Bill Amount\n[0]", 
                            font=("goudy old style", 15, "bold"), bg="#3f51b5", fg="white")
        self.lbl_amnt.place(x=2, y=5, width=120, height=70)

        self.lbl_discount = Label(self.billMenuFrame, text="Discount\n[5%]", 
                                font=("goudy old style", 15, "bold"), bg="#8bc34a", fg="white")
        self.lbl_discount.place(x=124, y=5, width=120, height=70)

        self.lbl_net_pay = Label(self.billMenuFrame, text="Net Pay\n[0]", 
                               font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white")
        self.lbl_net_pay.place(x=246, y=5, width=160, height=70)

        btn_print = Button(self.billMenuFrame, text="Print", cursor="hand2", command=self.print_bill,
                         font=("goudy old style", 15, "bold"), bg="lightgreen", fg="white")
        btn_print.place(x=2, y=80, width=150, height=50)

        btn_clear_all = Button(self.billMenuFrame, text="Clear All", command=self.clear_all,
                             font=("goudy old style", 15, "bold"), bg="gray", fg="white")
        btn_clear_all.place(x=154, y=80, width=120, height=50)

        btn_generate = Button(self.billMenuFrame, text="Generate/Save Bill", command=self.generate_bill,
                            font=("goudy old style", 15, "bold"), bg="#009688", fg="white")
        btn_generate.place(x=276, y=80, width=130, height=50)

        # Footer
        self.footer = Label(self.root, text="IMS - Inventory Management System | Developed by Parag",
                          font=("times new roman", 11), bg="#4d636d", fg="white")
        self.footer.pack(side=BOTTOM, fill=X)

        self.show()
        self.update_date_time()

#====================All Functions in ===================================================================
    def get_input(self, num):
        xnum = self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)
    
    def clear_cal(self):
        self.var_cal_input.set('')
    
    def perform_cal(self):
        result = self.var_cal_input.get()
        self.var_cal_input.set(eval(result))

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT pid, name, Price, Qty, Status FROM Product WHERE status='Active'")
            rows = cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in rows:
                self.product_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_Search.get() == "":
                messagebox.showerror("Error", "Search input is required", parent=self.root)
            else:
                cur.execute("SELECT pid, name, Price, Qty, Status FROM Product WHERE name LIKE '%" + self.var_Search.get() + "%' AND status='Active'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                        self.product_Table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.product_Table.focus()
        content = self.product_Table.item(f)
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_Price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock [{str(row[3])}]")
        self.var_Stock.set(row[3])
        self.var_Qty.set('1')

    def get_data_cart(self, ev):
        f = self.Cart_Table.focus()
        content = self.Cart_Table.item(f)
        row = content['values']
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_Price.set(row[2])
        self.var_Qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock [{str(row[4])}]")
        self.var_Stock.set(row[4])

    def add_update_cart(self):
        if self.var_pid.get() == '':
            messagebox.showerror("Error", "Please select Product from the list", parent=self.root)
        elif self.var_Qty.get() == '':
            messagebox.showerror("Error", "Quantity is Required", parent=self.root)
        elif int(self.var_Qty.get()) > int(self.var_Stock.get()):
            messagebox.showerror("Error", "Invalid Quantity", parent=self.root)
        else:
            price_cal = float(self.var_Price.get())
            cart_data = [self.var_pid.get(), self.var_pname.get(), price_cal, self.var_Qty.get(), self.var_Stock.get()]
            
            # Update cart
            present = 'no'
            index = 0
            for row in self.cart_list:
                if self.var_pid.get() == row[0]:
                    present = 'yes'
                    break
                index += 1
            
            if present == 'yes':
                op = messagebox.askyesno('Confirm', "Product already present\nDo you want to Update/Remove from the Cart list", parent=self.root)
                if op:
                    if self.var_Qty.get() == "0":
                        self.cart_list.pop(index)
                    else:
                        self.cart_list[index][3] = self.var_Qty.get()
            else:
                self.cart_list.append(cart_data)
            
            self.show_cart()
            self.bill_updates()

    def show_cart(self):
        try:
            self.Cart_Table.delete(*self.Cart_Table.get_children())
            for row in self.cart_list:
                self.Cart_Table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def bill_updates(self):
        self.bill_amnt = 0
        self.net_pay = 0
        self.discount = 0
        for row in self.cart_list:
            self.bill_amnt = self.bill_amnt + (float(row[2]) * int(row[3]))
        
        self.discount = (self.bill_amnt * 5) / 100
        self.net_pay = self.bill_amnt - self.discount
        self.lbl_amnt.config(text=f'Bill Amount\n{str(self.bill_amnt)}')
        self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
        self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")

    def generate_bill(self):
        if self.var_cname.get() == '' or self.var_contact.get() == '':
            messagebox.showerror("Error", "Customer Details are required", parent=self.root)
        elif len(self.cart_list) == 0:
            messagebox.showerror("Error", "Please add product to the Cart!!!", parent=self.root)
        else:
            # Bill Top
            self.bill_top()
            # Bill Middle
            self.bill_middle()
            # Bill Bottom
            self.bill_bottom()
            
            # Create bill directory if it doesn't exist
            if not os.path.exists('bill'):
                os.makedirs('bill')
                
            fp = open(f'bill/{str(self.invoice)}.txt', 'w')
            fp.write(self.txt_bill_area.get('1.0', END))
            fp.close()
            messagebox.showinfo('Saved', "Bill has been generated/Save in Backend", parent=self.root)
            self.chk_print = 1

    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''
\t\tXYZ-Inventory
\t Phone No. 98725***** , Delhi-125001
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0', END)
        self.txt_bill_area.insert('1.0', bill_top_temp)

    def bill_bottom(self):
        bill_bottom_temp = f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.txt_bill_area.insert(END, bill_bottom_temp)

    def bill_middle(self):
        for row in self.cart_list:
            name = row[1]
            qty = row[3]
            price = float(row[2]) * int(row[3])
            price = str(price)
            self.txt_bill_area.insert(END, "\n " + name + "\t\t\t" + qty + "\tRs." + price)

    def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_Price.set('')
        self.var_Qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_Stock.set('')

    def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0', END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_Search.set('')
        self.clear_cart()
        self.show()
        self.show_cart()
        self.chk_print = 0

    def update_date_time(self):
        time_now = time.strftime("%I:%M:%S")
        date_now = time.strftime("%d-%m-%Y")
        self.lal_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_now)}\t\t Time: {str(time_now)}")
        self.lal_clock.after(200, self.update_date_time)

    def print_bill(self):
        if self.chk_print == 1:
            messagebox.showinfo('Print', "Please wait while printing", parent=self.root)
            new_file = tempfile.mktemp('.txt')
            open(new_file, 'w').write(self.txt_bill_area.get('1.0', END))
            os.startfile(new_file, 'print')
        else:
            messagebox.showerror('Print', "Please generate bill, to print the receipt", parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")
        if __name__ == "_main_":
            root = Tk()
            obj = BILLINGCLASS(root)
            root.mainloop()  
