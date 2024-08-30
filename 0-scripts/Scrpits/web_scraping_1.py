import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.worldometers.info/world-population/population-by-country/'
response = requests.get(url)


soup = BeautifulSoup(response.content, 'html.parser')
table = soup.find('table')


headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())


rows = []


for row in table.find_all('tr')[1:]:
    columns = row.find_all('td')
    row_data = [col.text.strip() for col in columns]
    rows.append(row_data)

df = pd.DataFrame(rows, columns=headers)

df.to_csv(r'D:\Creativa\90H\Final\Requirements\1-webscraping\scraped1.csv',index=False)

print("Web Scraping Done!")
