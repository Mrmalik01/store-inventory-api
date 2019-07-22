import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users  (id INTEGER PRIMARY KEY, username TEXT, password TEXT)'
cursor.execute(create_table)

create_item_table = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)'
cursor.execute(create_item_table)

connection.commit()
connection.close()