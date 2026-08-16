import requests 
from bs4 import BeautifulSoup 
URL="https://www.avito.ma/fr/rabat/appartements-%C3%A0_vendre"
headers={"User-Agent":"Mozilla/5.0"}
response=requests.get(URL,headers=headers,timeout=20)
print(response.status_code)
soup=BeautifulSoup(response.text,"html.parser")
print(soup.title)
