# https://github.com/sqlitebrowser/sqlitebrowser/releases/tag/v3.9.1

import sqlite3

# if it attempts to connect to a non-existent
# database, it creates it
conn = sqlite3.connect('tutorial.db')
# defines the connection in the "CURSOR"

# the CURSOR itself
c = conn.cursor()

# create table
def create_table():

    # inside stufftoplot = columns and datatypes of those columns
    # e.g. UNIX timestamp, type = REAL (python float)
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, \
    keyword TEXT, value REAL)')
    # in general, ALL CAPS for things that are pure SQL (best practice)

    ###
    ### stuffToPlot is the name of the 'table' with the arguments in
    # the parenthesis as its columns
    #check DB Browser for SQLite

# columns here correspond to the same columns @ create_table
def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(2131231231, '2016-01-01', \
    'Python', 5)")

    # save db
    conn.commit()   # commit to db
    c.close()       # close cursor
    conn.close()    # stop memory from being used, not essential

create_table()
data_entry()