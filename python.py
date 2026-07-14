import books
import members
import issues

def menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Search Books")
    print("5. List Books")
    print("6. Add Member")
    print("7. Delete Member")
    print("8. List Members")
    print("9. Issue Book")
    print("10. Return Book")
    print("11. Overdue Books")
    print("12. List Issues")
    print("0. Exit")

def run():
    while True:
        menu()
        ch = input("Enter choice: ").strip()
        if ch == "1":
            t = input("Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            q = int(input("Quantity: "))
            books.add_book(t, a, i, q)
        elif ch == "2":
            bid = int(input("Book ID: "))
            t = input("Title: ")
            a = input("Author: ")
            q = int(input("Quantity: "))
            books.update_book(bid, t, a, q)
        elif ch == "3":
            bid = int(input("Book ID: "))
            books.delete_book(bid)
        elif ch == "4":
            k = input("Search keyword: ")
            for r in books.search_books(k):
                print(r)
        elif ch == "5":
            for r in books.list_books():
                print(r)
        elif ch == "6":
            n = input("Name: ")
            e = input("Email: ")
            p = input("Phone: ")
            members.add_member(n, e, p)
        elif ch == "7":
            mid = int(input("Member ID: "))
            members.delete_member(mid)
        elif ch == "8":
            for r in members.list_members():
                print(r)
        elif ch == "9":
            bid = int(input("Book ID: "))
            mid = int(input("Member ID: "))
            ok = issues.issue_book(bid, mid)
            print("Issued." if ok else "Book not available.")
        elif ch == "10":
            iid = int(input("Issue ID: "))
            ok = issues.return_book(iid)
            print("Returned." if ok else "Invalid or already returned.")
        elif ch == "11":
            for r in issues.overdue_books():
                print(r)
        elif ch == "12":
            for r in issues.list_issues():
                print(r)
        elif ch == "0":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()
