import pymysql

#database connection
connection = pymysql.connect(host="localhost",user="root",passwd="",database="Employee")
cursor = connection.cursor()
# some other statements  with the help of cursor
print("Database connected successfully")
connection.close()

