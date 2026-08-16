import pandas as pd 
import cloudscraper 
from bs4 import BeautifulSoup

def get_detail_location(url,scraper):
    response=scraper.get(url)
    soup=BeautifulSoup(response.text,"html.parser")
    location=soup.select_one("span.sc-16573058-17.gLkxLA")
    if location:
        return location.get_text(strip=True)
    else:
        return "Not Specified" 

URL="https://www.avito.ma/fr/rabat/appartements-%C3%A0_vendre"
MAX_PAGES=20
scraper=cloudscraper.create_scraper(browser={"browser":"firefox","platform":"linux","mobile":False})
listings=[]
for page in range(1,MAX_PAGES+1):
    url=f"{URL}?o={page}"
    response=scraper.get(url)
    print(page,response.status_code)
    soup=BeautifulSoup(response.text,"html.parser")
    cards = soup.select('a[data-testid^="ad-card-v2-"]')
    for card in cards:
        try :
            listing_url=card.get("href")
            surface=card.select_one('span[title="Surface totale"]')
            if surface:
                surface=surface.get_text(strip=True)
            else:
                surface="Not Specified"
            chambres=card.select_one('span[title="Chambres"]')
            if chambres:
                chambres=chambres.get_text(strip=True)
            else:
                chambres="Not Specified"
            sdb=card.select_one('span[title="Salle de bain"]')
            if sdb:
                sdb=sdb.get_text(strip=True)
            else:
                sdb="Not Specified"
            etage=card.select_one('span[title="Étage"]')
            if etage:
                etage=etage.get_text(strip=True)
            else:
                etage="Not Specified"
            location=card.select_one("span.sc-j5d10c-23.gPApYa")
            if location:
                location=location.get_text(strip=True)
            else:
                location="Not Specified"
            if("," not in location or  location=="Not Specified") and listing_url:
                location=get_detail_location(listing_url,scraper)
            prix=card.select_one("span.sc-b6852cba-2.dFgooy")
            if prix:
                prix=prix.get_text(strip=True)
            else:
                prix="Not Specified"
            listing={"surface":surface,
                 "chambres":chambres,
                 "sdb":sdb,
                 "etage":etage,
                 "location":location,
                 "prix":prix}
            listings.append(listing)
        except Exception as e:
            print(f"Error:{e}")

df=pd.DataFrame(listings)
df.to_csv("sale_20.csv",index=False,encoding="utf-8")


