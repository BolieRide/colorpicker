# Importing the required modules
import os
import sys
import lxml
import pandas as pd
from bs4 import BeautifulSoup

input = "D:\PDM_Class\colorpicker\dakkadakka.html"

with open(input, 'r') as f:
    contents = f.read()

# for getting the header from
# the HTML file
list_header = []
soup = BeautifulSoup(contents, 'lxml')
division = soup.find(id="header")
for td in division.find_all("td"):
    try:
        shead = str(td.get_text())
        shead2 = shead.replace("\n", "")
        list_header.append(shead2)
        print(list_header)
    except:
        continue

# Storing the data into Pandas
df = pd.read_html(input)
df2 = df[-1]
df2.reset_index(drop=True)
df2.columns = list_header
df2 = df2.iloc[1:,:]
df2 = df2.replace(['\ufffd'], '-')
df2.pop(' Colour')
df2.pop(' Rackham')
df2.pop(' INSTAR Vintage')
df2.pop(' INSTAR 6')
df2.set_index(df2.pop(' Hex Code'), inplace=True)
df2.reset_index(inplace=True)
df2[' Hex Code'] = df2[' Hex Code'].apply('="{}"'.format)
print(df2)
df2.to_csv('dakka.csv')