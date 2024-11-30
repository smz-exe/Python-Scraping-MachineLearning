from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as parse

url = 'http://api.aoikujira.com/zip/xml/1500042'

res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')

ken = soup.find('ken').string
shi = soup.find('shi').string
cho = soup.find('cho').string
disp = soup.find('disp').string
api = soup.find('api').string
print(res)
print(ken, shi, cho)
print("disp=", disp)
print("api=", api)


api = 'http://api.aoikujira.com/zip/xml/get.php'

values = {
    'fmt': 'xml',
    'zn': '1500042'
}

params = parse.urlencode(values)

url = api + "?" + params
print('url=', url)
data = req.urlopen(url).read()
text = data.decode("utf-8")
print(text)
