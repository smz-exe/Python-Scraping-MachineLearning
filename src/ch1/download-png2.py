import urllib.request

url = 'https://uta.pw/shodou/img/28/214.png'
savename = 'test2.png'

mem = urllib.request.urlopen(url).read()

with open(savename, mode='wb') as f:
    f.write(mem)
    print('file saved as', savename)