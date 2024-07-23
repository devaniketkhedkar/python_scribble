import pandas as pd
import xlsxwriter
import configparser
import mysql.connector
import paths
config = configparser.ConfigParser()
config.read('D:\\My_Learning\Python\ConfigFiles\\db_config.ini')

conn=mysql.connector.connect(host=config['mydb']['host'],user=config['mydb']['user'],passwd=config['mydb']['password'])

# SQL query
sql_query = "select * from demodb.customers"

# Execute query and save to DataFrame
df = pd.read_sql_query(sql_query, conn)
file_name_path= paths.file_path + 'output11.xlsx'
print("File Name and Path : " + file_name_path)
# Write DataFrame to Excel
df.to_excel(file_name_path, index=False)

# Close the connection
conn.close()
