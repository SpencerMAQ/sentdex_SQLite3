# 5th SQLite tutorial
# point of NO RETURN (DELETES UPDATES)
# UPDATE, DELETE = PERMANENT

import sqlite3
import time         # unix and sleep
import datetime     # time/datestamp
import random
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')    # dunno what this does #graphics probably

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
    c.execute('''CREATE TABLE IF NOT EXISTS stuffToPlot
                            (unix REAL,
                            datestamp TEXT,
                            keyword TEXT,
                            value REAL)'''
              )
    # in general, ALL CAPS for things that are pure SQL (best practice)

    ###
    ### stuffToPlot is the name of the 'table' with the arguments in
    # the parenthesis as its columns
    #check DB Browser for SQLite

# columns here correspond to the same columns @ create_table
def data_entry():
    c.execute('''INSERT INTO stuffToPlot
                    VALUES(
                    2131231231,
                    '2016-01-01',
                    'Python',
                    5)'''
              )

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
    c.execute('''INSERT INTO stuffToPlot (unix, datestamp, keyword, value)
                    VALUES (?, ?, ?, ?)''',
                    (unix, date, keyword, value)
              )
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
    #c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python'")
    c.execute('''SELECT * FROM stuffToPlot
                    WHERE unix > 1498312457'''
              )
    # think of the 'cursor' as doing some actual selection on the db
    # SELECT ONLY SELECTS, c.fetchall does the COPY

    ### in order to SELECT the columns in different order
    # any order not nec same as the data_entry
    #c.execute("SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE value=3")

    # c.fetchone() only single row      ## SAMPLE 1
    ##data = c.fetchall()               ## SAMPLE 1

    ##print(data)                       ## SAMPLE 2
    ### prints a dictionary of tuples   ## SAMPLE 2
    for row in c.fetchall():
        print(row)

def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        # row[0] = unix, 1 = VALUE
        #print(row[0])
        #print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    ## '-' = line style
    ## check tooltip
    plt.plot_date(dates, values, '-')
    plt.show()


def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

    # c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')
    #
    # conn.commit()
    #
    # c.execute('SELECT * FROM stuffToPlot')
    # [print(row) for row in c.fetchall()]

    # How to get rid of everything that has a VALUE = 99
    c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    # to limit, type after value = 99, LIMIT 50 (only for MySQL, not SQLite)
    conn.commit()
    # print(50*'#')

    ## Note however that you might want to print first what you're about to delete
    ## and the length of the list beofre you delete it
    ## And ask the user to confirm the deletion first
    # e.g.
    # c.execute('SELECT * From stuffToPlot WHERE value = 2')
    # print(len(c.fetchall()))

    c.execute('SELECT * FROM stuffToPlot')
    [print(row) for row in c.fetchall()]

del_and_update()

#graph_data()

#create_table()
#data_entry()
#for i in range(10):
#    dynamic_data_entry()
#    time.sleep(1)
#    # sleep = only fur the purpose of illustration so that the timestamp would go up by 1 second
#    print(i)

#read_from_db()
c.close()
conn.close()