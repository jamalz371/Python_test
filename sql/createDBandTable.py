import sqlite3

conn = sqlite3.connect('test.db')

print "Database successfully created"

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

print "Table COMPANY successfully created"

conn.close()

