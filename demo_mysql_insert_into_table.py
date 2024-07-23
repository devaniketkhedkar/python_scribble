import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user@123",
  database="demodb"
)
mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")