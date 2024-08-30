import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_age_structure'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')

headers = ['Country', '0-14', '15-64', '65-100']

rows = []

for row in table.find_all('tr')[2:]:
    columns = row.find_all('td')
    row_data = [col.text.strip() for col in columns]
    rows.append(row_data)

df = pd.DataFrame(rows, columns=headers)

df.to_csv(r'D:\Creativa\90H\Final\Requirements\1-webscraping\scraped4.csv',index=False)

print("Web Scraping Done!")
