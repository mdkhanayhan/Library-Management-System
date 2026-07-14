# Library Management System

A command-line Library Management System built with Python and MySQL. Supports book inventory, member records, and book issue/return tracking with overdue detection.

## Features

- Add, update, delete, and search books
- Add and delete members
- Issue books to members with automatic due date (14 days)
- Return books and track overdue issues
- MySQL-backed persistent storage

## Tech Stack

- Python 3
- MySQL
- `mysql-connector-python`

## Project Structure

```
library-management-system/
├── db.py           # MySQL connection setup
├── books.py         # Book CRUD operations
├── members.py        # Member CRUD operations
├── issues.py         # Issue/return logic
├── main.py          # CLI entry point
├── db_setup.sql       # Database schema
├── requirements.txt
└── README.md
```

## Setup

1. Install MySQL and create the schema:
```bash
mysql -u root -p < db_setup.sql
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Update credentials in `db.py`:
```python
host="localhost"
user="root"
password="your_password"
database="library_db"
```

4. Run the application:
```bash
python main.py
```

## Database Schema

- **books**: book_id, title, author, isbn, qty, available
- **members**: member_id, name, email, phone
- **issues**: issue_id, book_id, member_id, issue_date, due_date, return_date

## Future Improvements

- GUI using Tkinter or a web frontend
- Fine calculation for overdue books
- User authentication for librarian access
