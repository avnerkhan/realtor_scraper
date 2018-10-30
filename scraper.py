import bs4 as bs
import urllib.request as request
from selenium import webdriver


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
        for word in data.find_all(tag, class_=this_class):
            print(word.text)
    def click_button(self, target_button):
        check_click = self.driver.find_element_by_partial_link_text(target_button)
        if check_click is not None:
            check_click.click()
            return True
            print("Next Page pressed")
        return False
    def get_url(self):
        return self.driver.current_url

            
            
            

curr_url = 'https://www.dallashomerealty.com/search/results/?county=Collin&city=Plano&subdivision=all&type=res&list_price_min=150000&list_price_max=all&area_min=all&beds_min=all&baths_min=all&lot_size_min=all&year_built_min=all&amenities=all&lot_description=all&school_district=all&sort_latest=true&keyword=houses%20in%20plano&gclid=EAIaIQobChMIiMzr6-Gs3gIVBtbACh2MMg95EAAYASAAEgIaSPD_BwE'

while(True):
    print(curr_url)
    this_item = Webpage(curr_url)
    this_item.find('a','address', 'lxml')
    this_item.click_button("Next")
    curr_url = this_item.get_url()










