import bs4 as bs
import urllib.request as request
from selenium import webdriver




class Webpage:
    def __init__(self, target_link):
        self.target = target_link
        self.driver = webdriver.Chrome("drivers/chromedriver")
        self.driver.get(target_link)
    def dump(self, type):
        raw_data = request.urlopen(self.target).read()
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
            self.update_url()
            return True
        return False
    def go_back(self, back_class):
        back_button = self.driver.find_element_by_class_name(back_class)
        back_button.click()
        self.driver.refresh()
    def get_url(self):
        return self.driver.current_url
    def update_url(self):
        self.target = self.get_url()
    def close_driver(self):
        self.driver.close()

            













