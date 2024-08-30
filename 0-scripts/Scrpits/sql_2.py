import pymysql
import pandas as pd

path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned2.csv'
df = pd.read_csv(path)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mydatabase'
)

cursor = conn.cursor()

insert_query = """
INSERT INTO cleaned_2 (Country_or_dependency,
Total_Area_KM,
Total_Area_M,
Land_Area_KM,
Land_Area_M,
Percentage_World_Mass) 
VALUES (%s,%s,%s,%s,%s,%s)
"""

for index, row in df.iterrows():
    cursor.execute(insert_query, (row['Country_or_dependency'],
                                  row['Total_Area_KM'],
                                  row['Total_Area_M'],
                                  row['Land_Area_KM'],
                                  row['Land_Area_M'],
                                  row['Percentage_World_Mass']))

conn.commit()

cursor.close()
conn.close()

print("Data has been successfully inserted into the MySQL database.")
