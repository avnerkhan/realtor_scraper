import bs4 as bs
import sqlite3 as db
import urllib.request as request
from selenium import webdriver


class Webpage:
    def __init__(self, target):
        self.target = target
    def aggregate(self, type):
        raw_data = request.urlopen(self.target).read()
        better_data = bs.BeautifulSoup(raw_data, type)
        return better_data
    def find(self, tag, this_class , type):
        data = self.aggregate(type)
        for word in data.find_all(tag, class_=this_class):
            print(word.text)
    def click_button(self, target):
        pass
            
            
            


this_item = Webpage('https://www.dallashomerealty.com/search/results/?county=Collin&city=Plano&subdivision=all&type=res&list_price_min=150000&list_price_max=all&area_min=all&beds_min=all&baths_min=all&lot_size_min=all&year_built_min=all&amenities=all&lot_description=all&school_district=all&sort_latest=true&keyword=houses%20in%20plano&gclid=EAIaIQobChMIiMzr6-Gs3gIVBtbACh2MMg95EAAYASAAEgIaSPD_BwE')
#this_item.find("div", "row property results", 'lxml')
this_item.find('a','address', 'lxml')










