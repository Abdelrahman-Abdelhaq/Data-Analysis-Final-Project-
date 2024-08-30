import pymysql
import pandas as pd

path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned3.csv'
df = pd.read_csv(path)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mydatabase'
)

cursor = conn.cursor()

insert_query = """
INSERT INTO cleaned_3 (Year,
World_Population,
Percentage_Yearly_Change,
Net_change,
Population_Density) 
VALUES (%s,%s,%s,%s,%s)
"""

for index, row in df.iterrows():
    cursor.execute(insert_query, (row['Year'],
                                  row['World_Population'],
                                  row['Percentage_Yearly_Change'],
                                  row['Net_change'],
                                  row['Population_Density']))

conn.commit()

cursor.close()
conn.close()

print("Data has been successfully inserted into the MySQL database.")
