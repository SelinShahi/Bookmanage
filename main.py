from usermanagement import login, register
from book import Book
from database import connect
db = connect()
cursor = db.cursor()
def auth_menu():
    while True:
        print('1. Register')
        print('2. login')
        choice = input('How can I help you? : ')
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register(username , password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username , password):
                return True
        else:
            print('Invalid choice')
def show_menu():
    print('1.add book')
    print('2.show books')
    print('3.search books')
    print('4.delete books')
    print('5.EXIT')
def add_book():
    title = input('what is title of the book? : ')
    author = input('what is author of the book? : ')
    year = input('what is year of the book? : ')
    cursor.execute("INSERT INTO books (title, author, year) VALUES (%s, %s, %s)", (title, author, year))
    db.commit()
    print('added your book successfully')
def show_books():
    cursor.execute('SELECT title, author, year FROM books')
    rows = cursor.fetchall()
    if not rows:
        print('hhmp!!! Your library is empty')
    else:
        for row in rows:
            print(f"Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")
def search_book():
    search= input('what do you want to find? : ')
    cursor.execute("SELECT title, author, year FROM books WHERE title LIKE %s", (f"%{search}%",))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"Title: {row[0]}, Author: {row[1]}, Year: {row[2]}")
    else:
        print('This book is not available')
def delete_book():
    title = input('What is the name of the book? : ')
    cursor.execute("DELETE FROM books WHERE title = %s", (title,))
    db.commit()
    if cursor.rowcount > 0:
        print(f'{title} deleted')
    else:
        print(f'{title} did not find')
if auth_menu():
    while True:
        show_menu()
        choice = input('how can I help you? : ')
        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            search_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print('Your information saved... goodbye ')
            break
        else:
            print('your number is not available')