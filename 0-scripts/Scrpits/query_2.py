import pymysql
import pandas as pd

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mydatabase'
)

query = """
SELECT * from cleaned_3 ;
"""

df = pd.read_sql(query, conn)

csv_file_path = r'D:\Creativa\90H\Final\Requirements\3-sql\selected_cleaned_3.csv'
df.to_csv(csv_file_path, index=False)

conn.close()

print("Query result has been saved to a CSV file.")
