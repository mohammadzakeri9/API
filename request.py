#gheymat ha be Rial va Dollar
import requests
from bs4 import BeautifulSoup
#===============dollar===============
url = requests.get("https://www.tgju.org/profile/price_dollar_rl")
soup  = BeautifulSoup(url.text, "html.parser")
dollar_price = soup.find("span",class_="price").text

#===============EUR===============
url1 = requests.get("https://www.tgju.org/profile/price_eur")
soup1 = BeautifulSoup(url1.text, "html.parser")
eur_price = soup1.find("span",class_="price").text

#===============Gold ons===============
url2 = requests.get("https://www.tgju.org/profile/ons")
soup2 = BeautifulSoup(url2.text, "html.parser")
Gold_ons = soup2.find("span",class_="price").text

#===============Gold18===============
url3 = requests.get("https://www.tgju.org/profile/geram18")
soup3 = BeautifulSoup(url3.text, "html.parser")
Gold18 = soup3.find("span",class_="price").text

#===============Gold24===============
url4 = requests.get("https://www.tgju.org/profile/geram24")
soup4 = BeautifulSoup(url4.text, "html.parser")
Gold24 = soup4.find("span",class_="price").text

#===============imami coin===============
url5 = requests.get("https://www.tgju.org/profile/sekee")
soup5 = BeautifulSoup(url5.text, "html.parser")
Imami_coin = soup5.find("span",class_="price").text

#===============BTC===============
url6 = requests.get("https://www.tgju.org/profile/crypto-bitcoin")
soup6 = BeautifulSoup(url6.text, "html.parser")
BTC = soup6.find("span",class_="price").text

#===============berent oil===============
url7 = requests.get("https://www.tgju.org/profile/energy-brent-oil")
soup7 = BeautifulSoup(url7.text, "html.parser")
Berent = soup7.find("span",class_="price").text

#===============shakheskol bors===============
url8 = requests.get("https://www.tgju.org/profile/gc30")
soup8 = BeautifulSoup(url8.text, "html.parser")
Shakhes = soup8.find("span",class_="price").text

#===============output===============
print(f"Dollar : {dollar_price} Rial")
print(f"EUR : {eur_price} Rial")
print(f"Gold ons : {Gold_ons} Rial")
print(f"Gold18 : {Gold18} Rial")
print(f"Gold24 : {Gold24} Rial")
print(f"Imami coin : {Imami_coin} Rial")
print(f"BTC : {BTC} Dollar")
print(f"Naft berent : {Berent} Dollar")
print(f"Shakheskol bors : {Shakhes} Rial")