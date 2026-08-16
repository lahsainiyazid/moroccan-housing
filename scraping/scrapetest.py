import cloudscraper 
from bs4 import BeautifulSoup 
URL="https://www.avito.ma/fr/rabat/appartements-%C3%A0_vendre"
scraper=cloudscraper.create_scraper(browser={"browser":"firefox","platform":"linux","mobile":False})
response=scraper.get(URL)
print(response.status_code)
soup=BeautifulSoup(response.text,"html.parser")
print(soup.title)
