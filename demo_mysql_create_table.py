import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user@123"
 #database="demodb"
  
)
mycursor = mydb.cursor()

#Here DB name is given in Query NOT in mydb
mycursor.execute("CREATE TABLE demodb.customers (name VARCHAR(255), address VARCHAR(255))")