import pymysql

#open database connection
db = pymysql.connect("localhost","cisco","cisco","test")

#prepare a cursor object using cursor() method
cursor = db.cursor()

#prepare sql query to insert a record into the database

sql = " insert into pets(name,owner,age) values('%s','%s','%d')" %('Mac1','Mohan',20)

sql1 = "update pets set age = age + 1 where age < 12 "

try:
    #execute SQL query using execute() method
    cursor.execute(sql)
    cursor.execute(sql1)
    #commit your changes in the database
except:
    #rollback in case there is any error
    db.rollback()
else:
    db.commit()

#disconnect from server
db.close()

