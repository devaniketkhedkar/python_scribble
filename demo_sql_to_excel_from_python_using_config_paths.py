import pandas as pd
import sql_cred
import paths

# SQL query
sql_query = "select * from demodb.customers"

# Execute query and save to DataFrame
df = pd.read_sql_query(sql_query, sql_cred.mydb_config)
print(df)
file_name_path=paths.file_path + 'output122.xlsx'
print("File Name and Path : " + file_name_path)
# Write DataFrame to Excel
df.to_excel(file_name_path, index=False)

# Close the connectiondeactivate

sql_cred.mydb_config.close()
