import sqlite3 as db

class DBAction:
    def __init__(self, this_path):
        self.path = this_path
        pass
    def create_table(self, table_name):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("""""")
        pass
    def retrieve_from_db(self, table_name):
        pass
    def push_to_db(self, table_name):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("")


