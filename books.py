from db import get_conn

def add_book(title, author, isbn, qty):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, isbn, qty, available) VALUES (%s,%s,%s,%s,%s)",
                (title, author, isbn, qty, qty))
    conn.commit()
    cur.close()
    conn.close()

def update_book(book_id, title, author, qty):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=%s, author=%s, qty=%s WHERE book_id=%s",
                (title, author, qty, book_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_book(book_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE book_id=%s", (book_id,))
    conn.commit()
    cur.close()
    conn.close()

def search_books(keyword):
    conn = get_conn()
    cur = conn.cursor()
    q = f"%{keyword}%"
    cur.execute("SELECT * FROM books WHERE title LIKE %s OR author LIKE %s OR isbn LIKE %s", (q, q, q))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def list_books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
