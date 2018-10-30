import sqlite3 as db

class DBAction:
    def __init__(self, this_path):
        self.path = this_path
    def create_table(self, table_name):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE IF NOT EXISTS {} (
                address text,
                price int
            )""".format(table_name))
    def retrieve_from_db(self, table_name):
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM {}".format(table_name))
            return cursor.fetchall()
    def push_to_db(self, table_name, address, price):
        assert address is str
        assert price is int
        with db.connect(self.path) as connection:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO {} VALUES (?, ?)".format(table_name), (address, price))


