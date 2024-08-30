import pandas as pd

file_path = r'D:\Creativa\90H\Final\Requirements\1-webscraping/scraped3.csv'
df = pd.read_csv(file_path)

df.columns = ['Year', 'World_Population', 'Percentage_Yearly_Change', 'Net_change',
              'Population_Density']

df['World_Population'] = df['World_Population'].str.replace(',', '').astype(int)
df['Percentage_Yearly_Change'] = df['Percentage_Yearly_Change'].str.rstrip('%').astype(float)
df['Net_change'] = df['Net_change'].str.replace(',', '')
df['Net_change'] = pd.to_numeric(df['Net_change'], errors='coerce')

row_limit = 73

df = df.iloc[:row_limit]

cleaned_file_path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned3.csv'
df.to_csv(cleaned_file_path, index=False)


print("Data Cleaned !")
