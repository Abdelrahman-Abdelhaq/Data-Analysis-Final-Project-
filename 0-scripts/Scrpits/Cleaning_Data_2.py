import pandas as pd


file_path = r'D:\Creativa\90H\Final\Requirements\1-webscraping/scraped2.csv'
df = pd.read_csv(file_path)


df.drop(columns=['#'], inplace=True)


df.columns = ['Country_or_dependency', 'Total_Area_KM', 'Total_Area_M', 'Land_Area_KM',
              'Land_Area_M', 'Percentage_World_Mass']

df['Total_Area_KM'] = df['Total_Area_KM'].str.replace(',', '').astype(int)
df['Total_Area_M'] = df['Total_Area_M'].str.replace(',', '').astype(int)
df['Land_Area_KM'] = df['Land_Area_KM'].str.replace(',', '').astype(int)
df['Land_Area_M'] = df['Land_Area_M'].str.replace(',', '').astype(int)
df['Percentage_World_Mass'] = df['Percentage_World_Mass'].str.rstrip('%').astype(float)

cleaned_file_path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned2.csv'
df.to_csv(cleaned_file_path, index=False)

print("Data Cleaned !")
