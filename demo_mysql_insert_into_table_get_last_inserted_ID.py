import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user@123",
  database="demodb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()

print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("select * from demodb.customers");
for x in mycursor:
  print(x, "Row Id", mycursor.lastrowid)