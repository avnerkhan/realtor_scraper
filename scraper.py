import bs4 as bs
import urllib.request as request

raw_data = request.urlopen('https://pythonprogramming.net/').read()
better_data = bs.BeautifulSoup(raw_data, 'lxml')


print(better_data.title.text)