from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class Productclass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1110x500+220+130")
        self.root.title("Inventory Management System | Developed by Parag & Omkrish")
        self.root.config(bg="white")
        
        # Title
        Label(self.root, text="Product Management", font=("goudy old style", 30),
              bg="#184a45", fg="White", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=2)
        
        # Message
        Label(self.root, text="Product Management Module", font=("goudy old style", 20),
              bg="white").pack(pady=100) 