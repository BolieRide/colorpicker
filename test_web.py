import requests
from bs4 import BeautifulSoup
import html2text

url = "https://encycolorpedia.com/"
hex = "#986532"

check = requests.get(url+hex.strip('#'), verify=False)
soup = BeautifulSoup(check.text, 'html.parser')
chunk = str(soup.find(id='information'))
color = html2text.html2text(chunk)
start = ".svg)"
end ="*."
idx1 = color.index(start)
idx2 = color.index(end)
print(color[idx1 + len(start) : idx2].strip("\n"))

