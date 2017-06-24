# 2nd SQLite tutorial

import sqlite3
import time         # unix and sleep
import datetime     # time/datestamp
import random

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

def dynamic_data_entry():
    unix = time.time()

    # create date stamp from time stamp
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    # strftime converts the specified time into a string format

    keyword = 'Python'
    value = random.randrange(0,10)

    # in the hard-coded data entry, the values were typed in
    # here we specify first the columns for our data entry
    c.execute('INSERT INTO stuffToPlot (unix, datestamp, keyword, value)' \
              'VALUES (?, ?, ?, ?)', (unix, date, keyword, value))
    # you can change the order of the columns
    # you can even leave some columns blank (SQL will not insert data for the col)

    ### the values inside the parentheses of stufftoplot will map onto
    # VALUES (?, ?, ?, ?)

    conn.commit()
    # you won't close c and conn here because this is dynamic
    # closing them everytime would waste resources
    # close them at the VERY end of the program instead


# read data from db
def read_from_db():

    # note that select everything is rarely done in SQL
    # you usually select 'bits'

    # SELECT * (select everything)
    #c.execute('SELECT * FROM stuffToPlot')
    # values e.g. keyword PYTHON vs Python = case sensitive
    c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python'")
    #c.execute("SELECT * FROM stuffToPlot WHERE unix > 1498312457")
    # think of the 'cursor' as doing some actual selection on the db

    ### in order to SELECT the columns in different order
    # any order not nec same as the data_entry
    #c.execute("SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE value=3")

    # c.fetchone() only single row      ## SAMPLE 1
    ##data = c.fetchall()               ## SAMPLE 1

    ##print(data)                       ## SAMPLE 2
    ### prints a dictionary of tuples   ## SAMPLE 2
    for row in c.fetchall():
        print(row)

#create_table()
#data_entry()
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
#    # sleep = only fur the purpose of illustration so that the timestamp would go up by 1 second
#    print(i)

read_from_db()
c.close()
conn.close()