

import pandas as pd

file_path = r'D:\Creativa\90H\Final\Requirements\1-webscraping/scraped4.csv'
df = pd.read_csv(file_path)

df.columns = ['Country_or_dependency', 'kids', 'adults', 'retired']

df['kids'] = df['kids'].str.rstrip('%').astype(float)
df['adults'] = df['adults'].str.rstrip('%').astype(float)
df['retired'] = df['retired'].str.rstrip('%').astype(float)


cleaned_file_path = r'D:\Creativa\90H\Final\Requirements\2-preprocessing (python)\cleaned4.csv'
df.to_csv(cleaned_file_path, index=False)


print("Data Cleaned !")
