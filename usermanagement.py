import re
import os
from database import connect
db = connect()
cursor = db.cursor()
def is_strong_password(password):
    if len(password) < 8:
        return False, 'Your password have to had 8 character'
    elif not re.search(r'[A-Z]' , password):
        return False, 'Your password have to had an upper word'
    elif not re.search(r'[a-z]' , password):
        return False, 'Your password have to had an lower word'
    elif not re.search(r'\d' , password):
        return False, 'Your password have to had a number'
    elif not re.search(r'[!@#$%^&*]' , password):
        return False, 'Your password have to had a character'
    return True, 'Your password is strong'
def register(username, password):
    valid , message = is_strong_password(password)
    if not valid:
        print(message)
        return

    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)' , (username, password))
        conn.commit()
        print(f'User {username} registered successfully.')
    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()
def login(username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    conn.close()

    if result:
        print(f'Welcome {username}')
        return True
    else:
        print("Invalid username or password")
        return False
    
