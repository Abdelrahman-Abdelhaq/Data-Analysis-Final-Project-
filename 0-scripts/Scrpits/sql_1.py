import pymysql
import pandas as pd

path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned1.csv'
df = pd.read_csv(path)

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mydatabase'
)

cursor = conn.cursor()

insert_query = """
INSERT INTO cleaned_1 (Country_or_dependency,
Population_2024,
Yearly_Change,
Net_Change,Density_PKm2
,Land_Area_Km2
,Migrants_net
,Fertility_Rate
,Median_Age
,Urban_Pop_Percentage
,World_Share) 
VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for index, row in df.iterrows():
    cursor.execute(insert_query, (row['Country_or_dependency'],
                                  row['Population_2024'],
                                  row['Yearly_Change'],
                                  row['Net_Change'],
                                  row['Density_PKm2'],
                                  row['Land_Area_Km2'],
                                  row['Migrants_net'],
                                  row['Fertility_Rate'],
                                  row['Median_Age'],
                                  row['Urban_Pop_Percentage'],
                                  row['World_Share']))

conn.commit()

cursor.close()
conn.close()

print("Data has been successfully inserted into the MySQL database.")
