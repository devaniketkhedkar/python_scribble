import pandas as pd
import mysql.connector  # or import pymysql

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="user",
    password="user@123",
)

# SQL query
sql_query = "select * from demodb.customers"

# Execute query and save to DataFrame
df = pd.read_sql_query(sql_query, conn)

# Write DataFrame to Excel
df.to_excel('output.xlsx', index=False)

# Close the connection
conn.close()
