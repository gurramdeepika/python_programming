import pymysql

#open database connection
db = pymysql.connect("localhost","cisco","cisco","test")

#prepare a cursor object using cursor() method
cursor = db.cursor()

#execute SQL query using execute() method
cursor.execute("SELECT VERSION()")

#fetch a single row using fetchone() method
data = cursor.fetchone()

print("Database version : %s " %data)

#disconnect from server
db.close()

