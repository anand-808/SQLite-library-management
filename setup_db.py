import sqlite3

def create_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    # Create books table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre TEXT NOT NULL,
        available INTEGER DEFAULT 1,
        borrowed INTEGER DEFAULT 0,  
        borrow_id INTEGER  
    )
    """)

    # Create users table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()
    print("SQLite database 'library.db' and necessary tables created successfully!")

create_database()