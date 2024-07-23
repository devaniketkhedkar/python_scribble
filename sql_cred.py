import mysql.connector

mydb_config = mysql.connector.connect(
  host="localhost",
  user="user",
  password="user@123",
)

# mydb_conn=mysql.connector.connect(mydb_config)