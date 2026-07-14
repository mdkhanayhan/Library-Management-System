from db import get_conn

def add_member(name, email, phone):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO members (name, email, phone) VALUES (%s,%s,%s)", (name, email, phone))
    conn.commit()
    cur.close()
    conn.close()

def delete_member(member_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM members WHERE member_id=%s", (member_id,))
    conn.commit()
    cur.close()
    conn.close()

def list_members():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM members")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
