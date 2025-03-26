from math import cos
from tkinter import *
from typing import Self
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
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

        # ===title====
        self.icon_title=PhotoImage(file="images/logo.png")
        title = Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT, font=("times new roman", 40, "bold"),bg="#0101c48",fg="white",anchor="w",padx=20).place(x=0, y=0, relwidth=1, height=70)  # Corrected
        #===btn_logout====
        Btn_logout=Button(self.root,command=self.logout,text="Logout",font=("times new romen",15,"blod"),bg="Yellow",cursor="hand2").place(x=1150,y=10,height=50,width=150)
        #===clock====
        self.lal_clock= Label(self.root, text="Welcome to Inventory Management System\t\t Date:DD/MM.YYYY\t\t Time:HH:MM:SS", font=("times new roman",15),bg="#4d636d",fg="white",anchor="w")
        self.lal_clock.place(x=0, y=70, relwidth=1, height=30)

        #====Product===========================================================
        
        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=6,y=110,width=410,height=550)
        ptitle=Label(ProductFrame1,text="All Product",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        #====Product Search================================================================
        self.var_Search=StringVar()
        ProductFrame2=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_search=Label(ProductFrame2,text="Search Product| by Name",font=("time new romen",15,"bold"),bg="white",fg="green").Place(X=2,Y=5)
 
        txt_search=Entry(ProductFrame2,textvariable=self.var_Search,font=("time new romen",15,),bg="lightyellow").Place(X=128,Y=44,width=150,height=22)

        btn_Search=Button(ProductFrame2,text="Search",command=self.Search,font=("goudy old style",15),bg="#2196f3",fg="white",cursor="hand2").Place(X=285,Y=45,width=100,height=25)

        btn_show_all=Button(ProductFrame2,text="Show All",command=self.show_all,font=("goudy old style",15),bg="#83531",fg="white",cursor="hand2").Place(X=285,Y=10,width=100,height=25)
  
        #===Product Frame Details===================================================

        cart_frame=Frame(ProductFrame1,bd=3,relief=RIDGE)
        cart_frame.place(x=2,y=140,width=398,height=375)

        Scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        Scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame1,columns=("pid","name","Price","Qty","Status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.product_Table.xview)
        Scrolly.config(command=self.product_Table.yview)


        self.product_Table.heading("pid",text="Pid")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("Price",text="Price")
        self.product_Table.heading("Qty",text="Qty")
        self.product_Table.heading("Status",text="Status")
        self.product_Table["show"]="headings"
        
        self.product_Table.column("Pid",width=40)
        self.product_Table.column("name",width=100)
        self.product_Table.column("Price",width=100)
        self.product_Table.column("Qty",width=40)
        self.product_Table.column("Status",width=90)
        
        
        self.product_Table.pack(fill=BOTH,expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data)

        lbl_note=Label(ProductFrame1,text="Note:Enter 0 Qty to remove Product from the Cart",font=("goudy old style",12),anchor="w",bg="white",fg="red").pack(side=BOTTOM,fill=X)

        #=====Customer Frame=========================================================================================================================================================
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=420,y=110,width=530,height=70)

        ctitle=Label(CustomerFrame,text="Customer Details",font=("goudy old style",20),bg="lightgray").pack(side=TOP,fill=X)
        
        lbl_name=Label(CustomerFrame,text=" Name",font=("time new romen",15),bg="white",fg="green").Place(X=5,Y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("time new romen",13,),bg="lightyellow").Place(X=80,Y=35,width=180)

        lbl_Contact=Label(CustomerFrame,text=" Contact No",font=("time new romen",15),bg="white",fg="green").Place(X=270,Y=35)
        txt_Contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("time new romen",13),bg="lightyellow").Place(X=380,Y=35,width=140)
       #====Cal Cart Frame====================================================
        Cal_Cart_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=420,y=190,width=530,height=360)
       
       #====Calculator Frame=============================================
        self.var_Cal_input=StringVar()

        Cal_Frame=Frame(Cal_Cart_Frame,bd=9,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=10,width=268,height=340)

        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_Cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state="readonly",justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn_7=Button(Cal_Frame,text='7',font=('arial',15,"bold"),command=lambda:self.get_input('7'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,columnspan=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,"bold"),command=lambda:self.get_input('8'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,columnspan=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,"bold"),command=lambda:self.get_input('9'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,columnspan=2)
        btn_sum =Button(Cal_Frame,text='+',font=('arial',15,"bold"),command=lambda:self.get_input('+'),bd=5,width=5,pady=10,cursor="hand2").grid(row=1,columnspan=3)

        btn_4=Button(Cal_Frame,text='4',font=('arial',15,"bold"),command=lambda:self.get_input('4'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,columnspan=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,"bold"),command=lambda:self.get_input('5'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,columnspan=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,"bold"),command=lambda:self.get_input('6'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,columnspan=2)
        btn_sum =Button(Cal_Frame,text='-',font=('arial',15,"bold"),command=lambda:self.get_input('-'),bd=5,width=5,pady=10,cursor="hand2").grid(row=2,columnspan=3)

        btn_1=Button(Cal_Frame,text='1',font=('arial',15,"bold"),command=lambda:self.get_input('1'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,columnspan=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,"bold"),command=lambda:self.get_input('2'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,columnspan=1)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,"bold"),command=lambda:self.get_input('3'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,columnspan=2)
        btn_mul =Button(Cal_Frame,text='*',font=('arial',15,"bold"),command=lambda:self.get_input('*'),bd=5,width=5,pady=10,cursor="hand2").grid(row=3,columnspan=3)
        
        btn_0=Button(Cal_Frame,text='0',font=('arial',15,"bold"),command=lambda:self.get_input('0'),bd=5,width=5,pady=15,cursor="hand2").grid(row=4,columnspan=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,"bold"),ommand=self.clear_cal,bd=5,width=5,pady=15,cursor="hand2").grid(row=4,columnspan=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,"bold"),command=self.perform_cal,bd=5,width=5,pady=15,cursor="hand2").grid(row=4,columnspan=2)
        btn_div =Button(Cal_Frame,text='/',font=('arial',15,"bold"),command=lambda:self.get_input('/'),bd=5,width=5,pady=15,cursor="hand2").grid(row=4,columnspan=3)

     #=====cart frame========================================== 
        cart_frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE)
        cart_frame.place(x=280,y=8,width=245,height=342)
        self.cartTitle=Label(cart_frame,text="Cart\t Total Product:[0]",font=("goudy old style",20,"bold"),bg="#262626",fg="white")
        self.cartTitle.pack(side=TOP,fill=X)


        Scrolly=Scrollbar(cart_frame,orient=VERTICAL)
        Scrollx=Scrollbar(cart_frame,orient=HORIZONTAL)

        self.Cart_Table=ttk.Treeview(cart_frame,columns=("pid","name","Price","Qty"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)
        Scrollx.pack(side=BOTTOM,fill=X)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrollx.config(command=self.Cart_Table.xview)
        Scrolly.config(command=self.Cart_Table.yview)

        self.CartTable.heading("pid",text="Pid")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("Price",text="Price")
        self.CartTable.heading("Qty",text="Qty")
        self.CartTable["show"]="headings"
        
        self.CartTable.column("Pid",width=40)
        self.CartTable.column("name",width=100)
        self.CartTable.column("Price",width=90)
        self.Cart_Table.column("Qty",width=40)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.Product_Table.bind("<ButtonRelease-1>",self.get_data_cart)

   #=====Add Cart widgets Frame==================================
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_Price=StringVar()
        self.var_Qty=StringVar()
        self.var_Stock=StringVar()
    
    Add_CartwidgetsFrame = Frame (self.root, bd=4, relief=RIDGE, bg="white")
    Add_CartwidgetsFrame.place(x=420,y=550,width=520,height=110)

    lbl_p_name=Label(Add_CartwidgetsFrame,Text="Product Name",font=("time new romen",15),bg="white"),Place(X=5,Y=5)
    txt_p_name=Entry(Add_CartwidgetsFrame,textvariable=Self.var_pname,font=("time new romen",15),bg="lightyellow",state="readonly"),Place(X=5,Y=35,width=190,height=22)

    lbl_p_price=Label(Add_CartwidgetsFrame,Text="Price per Qty",font=("time new romen",15),bg="white"),Place(X=230,Y=5)
    txt_p_price=Entry(Add_CartwidgetsFrame,textvariable=Self.var_Price,font=("time new romen",15),bg="lightyellow",state="readonly"),Place(X=230,Y=35,width=150,height=22)

    lbl_p_Qty=Label(Add_CartwidgetsFrame,Text="Quantity",font=("time new romen",15),bg="white"),Place(X=230,Y=5)
    txt_p_Qty=Entry(Add_CartwidgetsFrame,textvariable=Self.var_Qty,font=("time new romen",15),bg="lightyellow",state="readonly"),Place(X=390,Y=35,width=120,height=22)

    Self.lbl_inStock=Label(Add_CartwidgetsFrame,Text="In Stock",font=("time new romen",15),bg="white"),
    Self.lbl_inStock.place(X=5,Y=70)

    btn_clear_cart=Button(Add_CartwidgetsFrame,text="clear",command=Self.clear_cart,font=("time new romen",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
    btn_add_cart=Button(Add_CartwidgetsFrame,text="Add | Update Cart",command=Self.add_update_cart,font=("time new romen",15,"bold"),bg="Orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
  #===========Billing Area==========================================================================================
    billFrame=Frame(Self.root,bd=2,relief=RIDGE,bg="white")
    billFrame.place(x=953,y=110,width=410,height=410)

    Btitle=Label(billFrame,text="Customer Bill Area",font=("goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
    Scrolly=Scrollbar(billFrame,orient=VERTICAL)
    Scrolly.pack(side=RIGHT,fill=Y)

    Self.txt_bill_area=Text=billFrame,yscrollcommand=Scrolly.set
    Self.txt_bill_area.pack(fill=BOTH,expend=1)
    Scrolly.config.command=Self.txt_bill_area.yview

 #=======billing button=======================================================================
    billMenuFrame=Frame(Self.root,bd=2,relief=RIDGE,bg="white")
    billMenuFrame.place(x=953,y=520,width=410,height=140)

    self_lbl_amnt=Label(billMenuFrame,text="Bill Amount\n[0]",font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white" )
    self_lbl_amnt.place(x=2,y=5,width=120,height=70)

    self_lbl_discount=Label(billMenuFrame,text="Discount\n[5%]",font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white" )
    self_lbl_discount.place(x=124,y=5,width=120,height=70)

    self_lbl_net_pay=Label(billMenuFrame,text="Net_Pay\n[0]",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white" )
    self_lbl_net_pay.place(x=246,y=5,width=160,height=70)

    
    btn_print=Button(billMenuFrame,text="Print",cursor="hand2",command=Self.print_bill,font=("goudy old style",15,"bold"),bg="lightgreen",fg="white" )
    btn_print.place(x=2,y=80,width=150,height=50)

    
    btn_clear_all=Button(billMenuFrame,text="Clear All",command=Self.clear_all,font=("goudy old style",15,"bold"),bg="gray",fg="white" )
    btn_clear_all.place(x=246,y=5,width=120,height=50)

    
    btn_generate=Button(billMenuFrame,text="Generate /Save Bill",command=Self.generate_bill,font=("goudy old style",15,"bold"),bg="#009688",fg="white" )
    btn_generate.place(x=246,y=80,width=160,height=50)



    #======footer=============================================================
    footer=Label(Self.root,text=("IMS/ Invertory Mangement System | Devloped by Parag"),font=("time new romen",11),bg="#4d636d",fg="white").Pack(side=BOTTOM,fill=Y)

    Self.show()
    #self.Bill_Top()
    Self.update_date_time()

#====================All Functions in ===================================================================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)

        def clear_cal(self):
            self.var_cal_input.set('')

            def Perform_cal(self):
                result=self.var_cal_input.get()
                self.var_cal_input.set(eval(result))
#======================================================================================

            def show(self):
             con=sqlite3.connect(database=r'ims.db')
             cur=con.cursor()
             try:
              #self.product_Table=ttk.Treeview(productFrame3,columns=("pid","name","Price","Qty","Status"),yscrollcommand=Scrolly.set,xscrollcommand=Scrollx.set)

                
              cur.execute("Select pid,name,Price,Qty,Status from Product where and status= 'Active'")
              row=cur.fetchall()
              self.product_Table.delete(*self.product_Table.get_children())
              for row in row:
                   self.product_Table.insert('',END,value=row)

             except Exception as ex:
                  Message.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)

      #===================================================================================================================
       
def Search():
                    con=sqlite3.connect(database=r'ims.db')
                    cur=con.cursor()
try:
               
        if Self.var_Search("")=="":
                    messagebox.showerror("Erro","Search input should be requied",parent=Self.root)


        else:
                    chr.execute("Select pid,name,Price,Qty,Status from Product where Name LIKE '%'"+Self.var_Serach.get()+"%' and status= 'Active' ")
                    row=chr.fetchall()
                    if len(row)!=0:

                     Self.Product_Table.delete(*Self.Product_Table.get_children())
                    for row in row:
                        Self.Product_Table.insert('',END,value=row)

                    else:
                        messagebox.showerror("Error","NO record found!!!")


except Exception as ex:
                   Message.showerror("Error",f"Error due to:{str(ex)}",parent=Self.root)

 #=======================================================================================================

def get_data(self,ev):
                f=self.Product_Table.focus()
                content=(self.Product_Table.item(f))
                row=content['values']
                self.var_pid.set(row[''])
                self.var_pname.set(row[''])
                self.var_Price.set(row[''])
                self.lbl_inStock.config(Text=f"In Stock[{str(row[3])}]")
                self.var_Stock.set(row['3'])
                self.var_Qty.set('1')

def get_data_cart(self,ev):
                f=self.CartTable.focus()
                content=(self.CartTable.item(f))
                row=content['values']
                self.var_pid.set(row[0])
                self.var_pname.set(row[1])
                self.var_Price.set(row[2])
                self.var_Qty.set(row[3])
                self.lbl_inStock.config(Text=f"In Stock[{str(row[4])}]")
                self.var_Stock.set(row[4])

                                          
def Add_Update(self):
    if self.var_pid.get()=='':
          messagebox.showerror("Error","Please Product Name form the list",parent=self.root)
    elif self.var_Qty.get()=='':
          messagebox.showerror("Error","Quantity is Required",parent=self.root)
    elif int(self.var_Qty.get())>int(self.var_stock.get()):
          messagebox.showerror("Error"," Invaild Quantity ",parent=self.root)  

    else:
         # price_cal=int(self.var_quy.get())*float(self.var_price.get())
          # price_cal=float(price_cal)
          price_cal=self.var_price.get()


          cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_Qty.get(),self.var_Stock.get()]
  #======Update_cart===========================================================================
          present='no'
          index=0
          for row in self.cart_list:
                 if self.var_pid.get()==row[0]:
                    present='yes'
                    break
                 index_+=1
                 if present:'YES'
                 op=messagebox.askyesno('Confirm',"Product already present\n do you want yo Upadate | Remove form the Cart list",parent=self.root)
                 if op==True:
                        if self.var_qty.get()=="0":
                              self.cart_list.pop(index_)
                        else:
                            #  self.cart_list[index_][2]=price_cal #price
                              self.cart_list[index_][3]=self.var_Qty.get() #qty
          else:
                        self.cart_list.append(cart_data)
                        
                        
                        self.show_cart()
                        self.Bill.update()
 #=======Bill Update========================================================================================

    def Bill_update(self):
          self.Bill_amnt=0
          self.net_pay=0
          self.Discount=0
          for row in self.cart_list:
                self.Bill_amnt=self.Bill_amnt+(float(row[2])*int(row[3]))

                self.Discount(self.Bill_amnt*5)/100
                self. net_pay=self.Bill_amnt-self.Discount
                self.lbl_amnt.config(Text=f"Bill amnt\n{str(self.Bill_amnt)}")
                self.lbl_net_pay.config(Text=f"net_pay\n{str(self.net_pay)}")
                self.cartTitle.config(text="Cart\t Total Product:[{str(len(self.cart_list))}]")
          
               #(text="Cart\t Total Product:[{str(len(self.cart_list))}]") is correct ok

#========================================================================================================        
def show_cart(self):
    
    try:
              
              self.CartTable.delete(*self.CartTable.get_children())
              for row in self.cart_list:
                   self.CartTable.insert('',END,value=row)

    except Exception as ex:
                  Message.showerror("Error",f"Error due to:{str(ex)}",parent=self.root)
  
def  generate_bill(self):
      if self.var_cname.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error",f"Customer Details are required ",parent=self.root)
      elif len(self.cart_list)==0:
             messagebox.showerror("Error",f"Please add product to the cart are !!! ",parent=self.root)

      else:
            #====Bill Top===
            self.Bill_top()
            #====Bill Middle===
            self.Bill_Middle()
            #====Bill Bottle===
            self.Bill_Bottom()

            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showinfo('saved'"Bill has been generated/save in backend",perent=self.root)
            self.chk_print=1

    #===bill top==========================================================================
      def bill_top(self):
            self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%D%M%Y"))
            bill_top_temp=f'''
 \t\tXYZ-Inventory 
 \t Phone No. 98725***** , Mumbai-123000
 {str("="*47)} 
 Customer Name: {self.var_cname.get()} 
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))} 
 {str("="*47)}
 Product Name\t\t\tQTY\tPrice
 {str("="*47)} 
            '''
            self.txt_bill_area.delete('1.0',END)
            self.txt_bill_area.insert('1.0',bill_top_temp) 

#=====bill Bottom=====================================================================
def Bill_Bottom(self):
      Bill_Bottom_temp=f'''
{str("="*47)} 
Bill Amount\t\t\t\tRs.{self.bill_amnt} 
Discount\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n 
            '''
      self.txt_bill_area.insert(END,Bill_Bottom_temp)

#=====bill Middle====================
def Bill_Middle(self):
       con=sqlite3.connect(database=r'ims.db')
       cur=con.cursor()
try:
            for row in Self.cart_list:
                   pid=row[0]
                   name=row[1]
                   Qty=int(row[4])-int(row[3])
            if int(row[3])==int(row[3]):
                     status="InActive" 

            if int(row[3])!=int(row[4]):
                     status="Active"

            price=float(row[2])*int(row[3])
            price=str(price)
            Self.txt_bill_area.insert(END,"\n""+name+\t\t\t"+row[3]+"\tRs."+price)
       #====UPdate Qtyin product============================
            chr.execute("Update Product set Qty=?,status=?where pid=?",(
                   Qty,
                   status,
                   pid

            ))
            cos.commit()
            cos.close()
            Self.show()     
except Exception as ex:
                  Message.showerror("Error",f"Error due to:{str(ex)}",parent=Self.root)
                  


def clear_cart(self):
                self.var_pid.set('')
                self.var_pname.set('')
                self.var_Price.set('')
                self.var_Qty.set('')
                self.lbl_inStock.config(Text= f"In Stock")
                self.var_Stock.set('')
 
def clear_all(self):
      del self.cart_list[:]
      self.var_cname.set('')
      self.var_contact.set('')
      self.txt_bill_area.delete('1.0',END)
      self.cartTitle.config(text="Cart\t Total Product:[0]")
      self.var_search.set('')
      self.clear_cart()
      self.show()
      self.show_cart()
      
def update_date_time(self):
       time=time.strftime("%I:%M:%S")
       date=time.strftime("%D:%M:%Y")
       self.lal_clock.config(text=f"Welcome to Inventory Management System\t\t Date:{str(date)}\t\t Time:{str(time)}")
       self.lbl_clock.after(200,self.update_date_time)

def print_bill(self):
 if self.chk_print==1:
      messagebox.showinfo('print',"Please wait while printing",perent=self.root)
      new_file=tempfile.mktemp(".txt")
      open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
      os.startfile(new_file,'print')

 else:
    messagebox.showerror('print',"Please gernerate bill,to print the recepite",parent=self.root)

def logout(self):
       self.root.destroy()
       os.system("python login.py")
       if __name__=="_main_":

         root=Tk()
         obj = BILLINGCLASS(root)
         root.mainloop ()  
