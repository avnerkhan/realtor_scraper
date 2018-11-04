import bs4 as bs
import urllib.request as request
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException




class Webpage:
    def __init__(self, target_link):
        self.orginal = target_link
        self.driver = webdriver.Chrome("drivers/chromedriver")
        self.driver.get(target_link)
    def dump(self, type):
        raw_data = request.urlopen(self.driver.current_url).read()
        better_data = bs.BeautifulSoup(raw_data, type)
        return better_data
    def find(self, tag, this_class , type):
        data = self.dump(type)
        return_word = []
        for word in data.find_all(tag, class_=this_class):
            return_word.append(word.text)
        return return_word
    def find_class(self, class_name):
        my_classes = self.driver.find_elements_by_class_name(class_name)
        return my_classes
    def find_refs(self, tag):
        my_refs = self.driver.find_elements_by_tag_name(tag)
        return my_refs
    def click_button(self, target_button):
        check_click = self.driver.find_element_by_partial_link_text(target_button)
        if check_click is not None:
            check_click.click()
            return True
        return False
    def go_back(self):
        try:
            self.driver.get(self.orginal)
        except NoSuchElementException:
            pass
    def check_popup(self, popup_id):
        try:
            bad_popup = self.driver.find_element_by_id(popup_id)
            bad_popup.click()
            self.load_page()
        except NoSuchElementException:
            pass
    def load_page(self):
        self.driver.get(self.get_url())
    def get_url(self):
        return self.driver.current_url
    def close_driver(self):
        self.driver.close()


def parse_string(integer):
        return_int = ""
        for num in integer:
                try:
                        if int(num) in range(0, 9):
                                return_int += str(num)
                except:
                        pass
        return int(return_int)
        
def add_if_not_null(add_arr, word):
        if len(word) > 0:
                add_arr.append(word)












