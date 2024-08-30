import pymysql
import pandas as pd

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='mydatabase'
)

query = """
SELECT 
    cleaned_1.Country_or_dependency,
    Population_2024,
    Yearly_Change,
    Net_Change,
    Density_PKm2,
    Land_Area_Km2,
    Migrants_net,
    Fertility_Rate,
    Median_Age,
    Urban_Pop_Percentage,
    World_Share,
    Total_Area_KM,
    Total_Area_M,
    Land_Area_KM,
    Land_Area_M,
    Percentage_World_Mass,
    cleaned_4.kids,
    cleaned_4.adults,
    cleaned_4.retired
FROM 
    cleaned_1
JOIN 
    cleaned_2
ON 
    cleaned_1.Country_or_dependency = cleaned_2.Country_or_dependency
JOIN
    cleaned_4
ON
    cleaned_1.Country_or_dependency = cleaned_4.Country_or_dependency;

"""

df = pd.read_sql(query, conn)

csv_file_path = r'D:\Creativa\90H\Final\Requirements\3-sql\cleaned_joined.csv'
df.to_csv(csv_file_path, index=False)

conn.close()

print("Query result has been saved to a CSV file.")
