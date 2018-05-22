#!/usr/bin/python

import pymysql

print ("Hello, Python!")

# Open database connection
db = pymysql.connect("localhost","root","deepak","cpp" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM cpp.customer"

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row[1])
except:
    print ("Error")

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
