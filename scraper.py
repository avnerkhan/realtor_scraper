import bs4 as bs
import urllib.request as request
from selenium import webdriver
from gather import DBAction
from nlp import Analyzer


class Webpage:
    def __init__(self, target_link):
        self.target = target_link
        self.driver = webdriver.Chrome("drivers/chromedriver")
        self.driver.get(target_link)
    def aggregate(self, type):
        raw_data = request.urlopen(self.target).read()
        better_data = bs.BeautifulSoup(raw_data, type)
        return better_data
    def find(self, tag, this_class , type):
        data = self.aggregate(type)
        return_word = []
        for word in data.find_all(tag, class_=this_class):
            return_word.append(word.text)
        return return_word
    def click_button(self, target_button):
        check_click = self.driver.find_element_by_partial_link_text(target_button)
        if check_click is not None:
            check_click.click()
            self.update_url()
            return True
        return False
    def get_url(self):
        return self.driver.current_url
    def update_url(self):
        self.target = self.get_url()
    def close_driver(self):
        self.driver.close()

            
def show_me_data(db_path, table_name):
    curr_db = DBAction(db_path)
    shown_info = curr_db.retrieve_from_db(table_name)
    return shown_info       
            
def loop_me_all(curr_url, db_path, table_name):
    this_item = Webpage(curr_url)
    this_db = DBAction(db_path)
    this_db.create_table(table_name)
    is_running = True
    while(is_running):
        addresses = this_item.find('a','address', 'lxml')
        prices = this_item.find("a", "price", "lxml")
        for num in range(len(addresses)):
            print(addresses[num])
            print(prices[num])
            this_db.push_to_db(table_name, addresses[num], prices[num])
        is_running = this_item.click_button("Next")

#loop_me_all('https://www.dallashomerealty.com/search/results/?county=Collin&city=Plano&subdivision=all&type=res&list_price_min=150000&list_price_max=all&area_min=all&beds_min=all&baths_min=all&lot_size_min=all&year_built_min=all&amenities=all&lot_description=all&school_district=all&sort_latest=true&keyword=houses%20in%20plano&gclid=EAIaIQobChMIiMzr6-Gs3gIVBtbACh2MMg95EAAYASAAEgIaSPD_BwE', "db/dallas.db", "all")
print(show_me_data("db/dallas.db", "all"))













