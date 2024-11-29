import urllib.request
import urllib.parse

API = 'https://api.aoikujira.com/zip/xml/get.php'

values = {
    'fmt': 'xml',
    'zn': '1000005'
}
params = urllib.parse.urlencode(values)

url = API+ "?" + params
print('url=', url)

data = urllib.request.urlopen(url).read()
text = data.decode('utf-8')
print(text)