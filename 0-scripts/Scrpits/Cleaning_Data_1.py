import pandas as pd


file_path = r'D:\Creativa\90H\Final\Requirements\1-webscraping/scraped1.csv'
df = pd.read_csv(file_path)

df.drop(columns=['#'], inplace=True)

df.columns = ['Country_or_dependency', 'Population_2024', 'Yearly_Change', 'Net_Change',
              'Density_PKm2', 'Land_Area_Km2', 'Migrants_net', 'Fertility_Rate',
              'Median_Age', 'Urban_Pop_Percentage', 'World_Share']

df['Population_2024'] = df['Population_2024'].str.replace(',', '').astype(int)
df['Yearly_Change'] = df['Yearly_Change'].str.rstrip('%').astype(float)
df['Net_Change'] = df['Net_Change'].str.replace(',', '').astype(int)
df['Density_PKm2'] = df['Density_PKm2'].str.replace(',', '').astype(int)
df['Land_Area_Km2'] = df['Land_Area_Km2'].str.replace(',', '').astype(int)
df['Migrants_net'] = df['Migrants_net'].str.replace(',', '').replace('N.A.', '0').astype(int)
df['Fertility_Rate'] = df['Fertility_Rate'].replace('N.A.', '0').astype(float)
df['Median_Age'] = df['Median_Age'].replace('N.A.', '0').astype(int)
df['Urban_Pop_Percentage'] = df['Urban_Pop_Percentage'].str.rstrip('%').replace('N.A.', '0').astype(float)
df['World_Share'] = df['World_Share'].str.rstrip('%').astype(float)

cleaned_file_path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned1.csv'
df.to_csv(cleaned_file_path, index=False)

print("Data Cleaned !")
