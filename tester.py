from gather import DBAction
from scraper import Webpage
from nlp import Analyzer

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
        description = this_item.find('p','property-description','lxml')
        prices = this_item.find("a", "price", "lxml")
        other_info = this_item.find("ul", "" , 'lxml')
        for num in range(len(addresses)):
            print(addresses[num])
            print(description[num])
            print(prices[num])
            print(other_info[num])
            #this_db.push_to_db(table_name, addresses[num], description[num] ,prices[num])
        is_running = this_item.click_button("Next")

loop_me_all('https://www.dallashomerealty.com/search/results/?county=Collin&city=Plano&subdivision=all&type=res&list_price_min=150000&list_price_max=all&area_min=all&beds_min=all&baths_min=all&lot_size_min=all&year_built_min=all&amenities=all&lot_description=all&school_district=all&sort_latest=true&keyword=houses%20in%20plano&gclid=EAIaIQobChMIiMzr6-Gs3gIVBtbACh2MMg95EAAYASAAEgIaSPD_BwE', "db/dallas.db", "all")
#print(show_me_data("db/dallas.db", "all"))
