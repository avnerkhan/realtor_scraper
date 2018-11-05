from gather import DBAction, show_me_data
from scraper import Webpage, parse_string, add_if_not_null
from nlp import Analyzer
from selenium.common.exceptions import WebDriverException
from threading import Thread
   
            
def loop_me_all(curr_url, db_path, table_name):
    this_item = Webpage(curr_url)
    this_db = DBAction(db_path)
    this_db.create_table(table_name)
    is_running = True
    while(is_running):
        addresses = this_item.find('a','address', 'lxml')
        prices = this_item.find("a", "price", "lxml")
        other_info = this_item.find("ul", "" , 'lxml')
        for num in range(len(addresses)):
            other_array = other_info[num].split()
            print(other_array)
            if len(other_array) == 8:
                print(addresses[num])
                print(prices[num])
                print(other_array)
                this_db.push_to_db(table_name, addresses[num], prices[num], other_info[num])
        is_running = this_item.click_button("Next")

def scrape_sold(curr_url, db_path, table_name):
    this_item = Webpage(curr_url)
    prediction_set = DBAction(db_path)
    prediction_set.create_table_predict(table_name)
    is_running = True
    while is_running:
            count = 0
            photos = this_item.find_class("photo-wrap")
            while count < len(photos):
                curr_button = photos[count]
                try:
                        curr_button.click()
                        this_item.check_popup("acsFocusFirst")
                        this_item.load_page()
                        get_data(this_item, prediction_set ,table_name)
                        this_item.go_back()
                        this_item.check_popup("acsFocusFirst")
                        photos = this_item.find_class("photo-wrap")
                except:
                        pass
                count += 1
            is_running = this_item.click_button_class("next")
    this_item.close_driver()


def get_data(webpage, curr_db, table_name):
        data_items = webpage.find_class("data-value")
        other_data = webpage.find_class("summary-datapoint")
        prediction = webpage.find_class("key-fact-data")
        potential_data =[]
        for house in data_items:
                add_if_not_null(potential_data, house.text)
        for other in other_data:
                add_if_not_null(potential_data, other.text)
        for predict in prediction:
                add_if_not_null(potential_data, predict.text)
        try:

                beds = parse_string(potential_data[0])
                baths = parse_string(potential_data[1])
                sqft = parse_string(potential_data[2])
                time_to_foreclose = parse_string(potential_data[4])
                price = parse_string(potential_data[5])
                curr_db.push_to_db_predict(table_name,price  ,beds, baths, sqft,time_to_foreclose)
        except Exception as error:
                print(error)
                print(curr_db.retrieve_from_db(table_name))
                pass




if __name__ == "__main__":
        #Thread(target = loop_me_all('https://www.dallashomerealty.com/search/results/?county=Collin&city=Plano&subdivision=all&type=res&list_price_min=150000&list_price_max=all&area_min=all&beds_min=all&baths_min=all&lot_size_min=all&year_built_min=all&amenities=all&lot_description=all&school_district=all&sort_latest=true&keyword=houses%20in%20plano&gclid=EAIaIQobChMIiMzr6-Gs3gIVBtbACh2MMg95EAAYASAAEgIaSPD_BwE', "db/dallas.db", "all")).start()
        Thread(target = scrape_sold('https://www.realtor.com/soldhomeprices/Dallas_TX', 'db/predict.db', 'predict')).start()




