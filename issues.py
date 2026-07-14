from datetime import date, timedelta
from db import get_conn

def issue_book(book_id, member_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT available FROM books WHERE book_id=%s", (book_id,))
    row = cur.fetchone()
    if not row or row[0] <= 0:
        cur.close()
        conn.close()
        return False
    issue_date = date.today()
    due_date = issue_date + timedelta(days=14)
    cur.execute("INSERT INTO issues (book_id, member_id, issue_date, due_date) VALUES (%s,%s,%s,%s)",
                (book_id, member_id, issue_date, due_date))
    cur.execute("UPDATE books SET available = available - 1 WHERE book_id=%s", (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    return True

def return_book(issue_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT book_id, return_date FROM issues WHERE issue_id=%s", (issue_id,))
    row = cur.fetchone()
    if not row or row[1] is not None:
        cur.close()
        conn.close()
        return False
    book_id = row[0]
    cur.execute("UPDATE issues SET return_date=%s WHERE issue_id=%s", (date.today(), issue_id))
    cur.execute("UPDATE books SET available = available + 1 WHERE book_id=%s", (book_id,))
    conn.commit()
    cur.close()
    conn.close()
    return True

def overdue_books():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM issues WHERE return_date IS NULL AND due_date < %s", (date.today(),))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

def list_issues():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM issues")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
