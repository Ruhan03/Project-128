from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
headers = ['Name','Distance','Mass','Radius']
BrownDwarfs = []

page = requests.get(START_URL)
soup = BeautifulSoup(page.text,'html.parser')
tables = soup.find_all('table')

table = tables[7]  
rows = table.find_all('tr')
for row in rows:
    columns = row.find_all('td')
    star = []
    for cell in columns:
        star.append(cell.text.rstrip())
    BrownDwarfs.append(star)

Names = []
Distance = []
Mass = []
Radius = []

for i in range(1,len(BrownDwarfs)):
    Names.append(BrownDwarfs[i][0])
    Distance.append(BrownDwarfs[i][5])
    Mass.append(BrownDwarfs[i][7])
    Radius.append(BrownDwarfs[i][8])

df = pd.DataFrame(list(zip(Names,Distance,Mass,Radius)),columns = headers)
file = df.to_csv('BrownDwarfs.csv')