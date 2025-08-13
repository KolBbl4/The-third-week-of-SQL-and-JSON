import sqlite3

connect = sqlite3.connect('base.db')
cursor = connect.execute('''CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price INTEGER)''')
connect.commit()

user_data = ('Мыло', 30)  
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', user_data)  
connect.commit()

user_data = ('Компьютер', 258)  
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', user_data)  
connect.commit()

user_data = ('Машина', 750)  
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', user_data)  
connect.commit()

user_data = ('Дом', 100000)  
cursor.execute('INSERT INTO products (name, price) VALUES (?, ?)', user_data)  
connect.commit()

connect.close()