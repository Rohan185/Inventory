import sqlite3
import os

def setup_database():
    """Create the SQLite database and necessary tables if they don't exist"""
    conn = sqlite3.connect('ims.db')
    cursor = conn.cursor()
    
    # Create Employee table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employee(
        eid TEXT PRIMARY KEY,
        name TEXT,
        email TEXT,
        gender TEXT,
        contact TEXT,
        dob TEXT,
        doj TEXT,
        pass TEXT,
        utype TEXT,
        address TEXT,
        salary TEXT
    )
    ''')
    
    # Create Supplier table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Supplier(
        invoice TEXT PRIMARY KEY,
        name TEXT,
        contact TEXT,
        desc TEXT
    )
    ''')
    
    # Create Category table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Category(
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    ''')
    
    # Create Product table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Product(
        pid INTEGER PRIMARY KEY AUTOINCREMENT,
        Supplier TEXT,
        Category TEXT,
        name TEXT,
        price TEXT,
        qty TEXT,
        status TEXT
    )
    ''')
    
    # Check if an admin account exists, if not create a default one
    cursor.execute("SELECT * FROM Employee WHERE utype='Admin'")
    if not cursor.fetchone():
        cursor.execute(
            "INSERT INTO Employee(eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
            ('EMP1', 'Admin User', 'admin@example.com', 'Male', '1234567890', '01/01/2000', '01/01/2023', 'admin123', 'Admin', 'Admin Address', '50000')
        )
        print("Default admin account created. Username: EMP1, Password: admin123")
    
    # Create bill directory if it doesn't exist
    if not os.path.exists('bill'):
        os.makedirs('bill')
        print("Created 'bill' directory")
    
    conn.commit()
    conn.close()
    print("Database setup completed successfully.")

if __name__ == "__main__":
    setup_database() 