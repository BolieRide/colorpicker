import requests
from bs4 import BeautifulSoup
import html2text
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://encycolorpedia.com/"
hex = "#986532"

check = requests.get(url+hex.strip('#'), verify=False)
soup = BeautifulSoup(check.text, 'html.parser')
chunk = str(soup.find(id='information'))
color = html2text.html2text(chunk)
print(color)
# start = ".svg)"
# end ="*."
# idx1 = color.index(start)
# idx2 = color.index(end)
# print(color[idx1 + 31 : idx2].replace("\n"," ").replace("*",""))

