import os
import sqlite3

class DataBaseContoller:
    def __init__(self):
        self.database = sqlite3.connect(f"{os.getcwd()}/data/db.sqlite")
        self.cursor = self.database.cursor()
    
    def insert_new_invoice(self, invoice_tag):
        self.cursor.execute("""INSERT INTO invoices (invoice_tag) VALUES (?)""", (invoice_tag,))
        self.database.commit()

    def get_last_created_invoice(self):
        self.cursor.execute("SELECT * FROM invoices ORDER BY id DESC LIMIT 1")
        return self.cursor.fetchone()
