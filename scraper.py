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

            













