import bs4 as bs
import sqlite3 as db
import urllib.request as request

class Aggregator:
    def __init__(self, target):
        self.target = target
    def aggregate(self):
        raw_data = request.urlopen(self.target).read()
        better_data = bs.BeautifulSoup(raw_data, 'lxml')
        return better_data


this_item = Aggregator('https://www.w3schools.com/python/python_classes.asp')
print_this = this_item.aggregate()
print(print_this)








