from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.yahoo.com/quote/JPY=X/"
res = req.urlopen(url)

soup = BeautifulSoup(res, "html.parser")

price_element = soup.select_one(".livePrice")
if price_element:
    price = price_element['data-value']
    print(price)
    print('usd/jpy=', price)
else:
    print("Price element not found")
