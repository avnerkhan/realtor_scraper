import sqlite3 as db
import scraper as sp 

class DBAction:
    def __init__(self, url):
        self.curr_start = sp.Webpage(url)
        pass
    def create_table(self, table_name):
        pass
    def retrieve_from_db(self, path, table_name):
        pass
    def push_to_db(self, path, table_name):
        with db.connect(path) as connection:
            cursor = connection.cursor()
            cursor.execute("")


