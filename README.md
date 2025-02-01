# SQLite Library Management System

A modern desktop application for managing library operations built with Python and Tkinter using SQLite database.

## 🚀 Features

* User Authentication
  * Secure login and registration system
  * Password hashing using bcrypt
  * User session management

* Book Management
  * Add new books to the library
  * View all books with sorting and filtering options
  * Issue books to users
  * Return books with borrow ID
  * Delete books from the system
  * Track book availability status

* Modern GUI
  * Clean and intuitive interface
  * Responsive design
  * Color-coded status indicators
  * Search and filter functionality
  * Sortable book lists

* Database
  * SQLite database for data persistence
  * Automatic database setup
  * Secure data handling

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/anand-808/SQLite-library-management.git
cd library-management-system
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install bcrypt
```

## 🚀 Usage

1. Run the main application:
```bash
python main.py
```

The system will automatically:
- Check if the database exists
- Create the database and required tables if they don't exist
- Launch the main application

## 📁 Project Structure

- `main.py`: Entry point of the application
- `library.py`: Main application logic and GUI
- `setup_db.py`: Database initialization script
- `library.db`: SQLite database file (created automatically)

## 💻 System Requirements

- Python 3.7 or higher
- Tkinter (usually comes with Python)
- SQLite3

## 🔐 Security Features

- Password hashing using bcrypt
- Secure database operations
- Input validation and sanitization
