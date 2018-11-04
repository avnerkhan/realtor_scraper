import sqlite3 as db
from scraper import parse_string

class DBAction:
    def __init__(self, this_path):
        self.path = this_path
    def create_table_predict(self, table_name):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS '{}' (
                price int,
                beds int,
                baths int,
                sqft int,
                time int
            )""".format(table_name))
    def create_table(self, table_name):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS '{}' (
                address text,
                price int,
                beds int,
                baths int,
                mls int,
                sqft int
            )""".format(table_name))
    def retrieve_from_db(self, table_name):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM '{}'".format(table_name))
            return cursor.fetchall()
    def push_to_db_predict(self, table_name,price ,beds, bath, sqft, time_to_foreclose):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO '{}' VALUES (?, ?, ?, ?, ?)".format(table_name), (price,beds, bath, sqft, time_to_foreclose))
    def push_to_db(self, table_name, address, price, other):
        other_array = other.split()
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO '{}' VALUES (?, ?, ?, ?, ?, ?)".format(table_name), (address, parse_string(price), parse_string(other_array[0]), parse_string(other_array[2]), parse_string(other_array[4]), parse_string(other_array[6])))

def show_me_data(db_path, table_name):
    curr_db = DBAction(db_path)
    shown_info = curr_db.retrieve_from_db(table_name)
    return shown_info    