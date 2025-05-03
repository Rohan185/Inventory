import tkinter as tk
from tkinter import messagebox, StringVar
import sqlite3
import os
from PIL import Image, ImageTk
import time
from tkinter import ttk

class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1350x700+0+0")
        
        # Create a canvas for the background
        self.canvas = tk.Canvas(root, width=1350, height=700, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        
        # Load and set background image
        try:
            bg_image = Image.open("images/warehouse_bg.png")
            bg_image = bg_image.resize((1350, 700), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
        except Exception as e:
            print(f"Error loading background image: {e}")
            self.create_gradient()
        
        # Semi-transparent overlay for better readability
        self.canvas.create_rectangle(0, 0, 1350, 700, 
                                   fill='#000000', 
                                   stipple='gray50')
        
        # Title Frame with semi-transparent background
        title_frame = tk.Frame(root, bg="#2c3e50")
        title_frame.place(x=0, y=0, width=1350, height=100)
        
        # Logo
        try:
            logo_img = Image.open("images/logo.png")
            logo_img = logo_img.resize((80, 80), Image.Resampling.LANCZOS)
            self.logo = ImageTk.PhotoImage(logo_img)
            logo_label = tk.Label(title_frame, image=self.logo, bg="#2c3e50")
            logo_label.place(x=20, y=10)
        except:
            pass
            
        # Title
        title_label = tk.Label(title_frame, text="Inventory Management System", 
                             font=("Arial", 24, "bold"), bg="#2c3e50", fg="white")
        title_label.place(x=120, y=30)
        
        # Create a frame for the 3D effect
        self.shadow_frame = tk.Frame(root, bg='#1a1a1a')
        self.shadow_frame.place(x=-365, y=195, width=360, height=410)
        
        # Main login frame with 3D effect
        self.login_frame = tk.Frame(root, bg='#ffffff', bd=0)
        self.login_frame.place(x=-360, y=200, width=350, height=400)
        
        # Add glass effect to login frame
        glass_effect = tk.Frame(self.login_frame, bg='#ffffff', bd=0)
        glass_effect.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Add inventory-themed border
        self.canvas.create_rectangle(495, 195, 855, 605, 
                                   outline='#2c3e50', 
                                   width=2, 
                                   dash=(5, 5))
        
        # Login Title with 3D effect
        login_title = tk.Label(glass_effect, text="Login", 
                             font=("Arial", 24, "bold"), 
                             bg='#ffffff', fg="#2c3e50")
        login_title.place(x=0, y=30, relwidth=1)
        
        # Add inventory icon
        try:
            inventory_icon = Image.open("images/inventory_icon.png")
            inventory_icon = inventory_icon.resize((40, 40), Image.Resampling.LANCZOS)
            self.inventory_icon = ImageTk.PhotoImage(inventory_icon)
            icon_label = tk.Label(glass_effect, image=self.inventory_icon, bg='#ffffff')
            icon_label.place(x=155, y=80)
        except:
            pass
        
        # Variables
        self.EmployeeID = StringVar()
        self.password = StringVar()
        
        # Username with modern style
        tk.Label(glass_effect, text="Employee ID", 
                font=("Arial", 12, "bold"), bg='#ffffff', 
                fg="#2c3e50").place(x=30, y=140)
        self.eid_entry = tk.Entry(glass_effect, 
                                textvariable=self.EmployeeID, 
                                font=("Arial", 12), bd=2, 
                                relief=tk.SOLID,
                                highlightthickness=1,
                                highlightbackground="#2c3e50",
                                highlightcolor="#3498db")
        self.eid_entry.place(x=30, y=170, width=290, height=35)
        
        # Password with modern style
        tk.Label(glass_effect, text="Password", 
                font=("Arial", 12, "bold"), bg='#ffffff', 
                fg="#2c3e50").place(x=30, y=220)
        self.pass_entry = tk.Entry(glass_effect, 
                                 textvariable=self.password, 
                                 show="•", font=("Arial", 12), 
                                 bd=2, relief=tk.SOLID,
                                 highlightthickness=1,
                                 highlightbackground="#2c3e50",
                                 highlightcolor="#3498db")
        self.pass_entry.place(x=30, y=250, width=290, height=35)
        
        # Login Button with modern style and hover effect
        self.login_btn = tk.Button(glass_effect, text="Login", 
                                 command=self.login, 
                                 font=("Arial", 14, "bold"), 
                                 bg="#2c3e50", fg="white",
                                 bd=0, cursor="hand2", 
                                 activebackground="#34495e",
                                 relief=tk.RAISED,
                                 padx=20)
        self.login_btn.place(x=30, y=320, width=290, height=45)
        
        # Add hover effect
        self.login_btn.bind("<Enter>", self.on_enter)
        self.login_btn.bind("<Leave>", self.on_leave)
        
        # Footer with semi-transparent background
        footer_frame = tk.Frame(root, bg="#2c3e50")
        footer_frame.place(x=0, y=650, width=1350, height=50)
        
        footer_label = tk.Label(footer_frame, 
                              text="© 2024 Inventory Management System | Developed by Parag & Omkrish", 
                              font=("Arial", 10), bg="#2c3e50", fg="white")
        footer_label.place(x=0, y=0, width=1350, height=50)
        
        # Animate login frame with 3D rotation effect
        self.animate_login_frame()

    def create_gradient(self):
        """Fallback gradient background if image fails to load"""
        for i in range(700):
            color = f'#{int(240 - (i/700)*40):02x}{int(240 - (i/700)*40):02x}{int(240 - (i/700)*40):02x}'
            self.canvas.create_line(0, i, 1350, i, fill=color)

    def animate_login_frame(self):
        """Animate the login frame sliding in from the left"""
        x = -360
        while x < 500:
            # Update shadow position
            self.shadow_frame.place(x=x-5, y=195, width=360, height=410)
            # Update main frame position
            self.login_frame.place(x=x, y=200, width=350, height=400)
            # Create perspective effect
            self.canvas.create_rectangle(x-5, 195, x+355, 605, 
                                       outline='#2c3e50', 
                                       width=2, 
                                       dash=(5, 5))
            self.root.update()
            x += 20
            time.sleep(0.02)
            # Clear the perspective effect
            self.canvas.delete("all")
            try:
                self.canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")
            except:
                self.create_gradient()

    def on_enter(self, e):
        """Button hover effect with elevation"""
        self.login_btn.config(bg="#34495e", relief=tk.SUNKEN)
        self.login_btn.place(x=32, y=322, width=286, height=41)

    def on_leave(self, e):
        """Button leave effect"""
        self.login_btn.config(bg="#2c3e50", relief=tk.RAISED)
        self.login_btn.place(x=30, y=320, width=290, height=45)

    def login(self):
        """Handles user login and redirects to dashboard."""
        # Show loading animation with 3D effect
        loading_frame = tk.Frame(self.login_frame, bg='#ffffff', bd=2, relief=tk.RAISED)
        loading_frame.place(x=30, y=320, width=290, height=45)
        
        loading_label = tk.Label(loading_frame, text="Logging in...", 
                               font=("Arial", 12), bg='#ffffff', fg="#2c3e50")
        loading_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.update()
        
        with sqlite3.connect('ims.db') as con:
            cur = con.cursor()
            cur.execute("SELECT utype FROM Employee WHERE eid=? AND pass=?", 
                       (self.EmployeeID.get(), self.password.get()))
            user = cur.fetchone()

        if user is None:
            loading_frame.destroy()
            messagebox.showerror('Error', 'Invalid Username or Password', parent=self.root)
            self.login_btn.place(x=30, y=320, width=290, height=45)
        else:
            # Animate exit sliding to the right
            for i in range(20):
                self.shadow_frame.place(x=495+i*10, y=195, width=360, height=410)
                self.login_frame.place(x=500+i*10, y=200, width=350, height=400)
                self.root.update()
                time.sleep(0.02)
            self.root.destroy()
            os.system("python dashboard.py" if os.path.exists("dashboard.py") else "echo 'dashboard.py not found'")

if __name__ == "__main__":
    root = tk.Tk()
    obj = LoginSystem(root)
    root.mainloop()
