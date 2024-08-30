import pymysql
import pandas as pd
import numpy as np


path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned4.csv'
df = pd.read_csv(path)

df = df.dropna(subset=['Country_or_dependency'])
df = df.replace({np.nan: None})

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mydatabase'
)

cursor = conn.cursor()

insert_query = """
INSERT INTO cleaned_4 (Country_or_dependency, kids, adults, retired) 
VALUES (%s, %s, %s, %s)
"""

for index, row in df.iterrows():
    cursor.execute(insert_query, (row['Country_or_dependency'],
                                  row['kids'],
                                  row['adults'],
                                  row['retired']))


conn.commit()

cursor.close()
conn.close()

print("Data has been successfully inserted into the MySQL database.")
