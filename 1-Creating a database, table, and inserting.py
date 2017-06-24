import sqlite3

# if it attempts to connect to a non-existent
# database, it creates it
conn = sqlite3.connect('tutorial.db')
