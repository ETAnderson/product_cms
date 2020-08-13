import json
import os
from generic_database import GenericDatabase as gdb
import uuid

class Product():
    def __init__(self, product_name, qty):
        self.name = product_name
        self.id = uuid.uuid4()
        self.qty = int(qty)

    def save(self):
        productdb = Product.get_db()
        product_saved = productdb.set(self.id, self.name)
        if product_saved:
            print(f'{self.name} successfully added!')
            return True
        return False

    def buy(self, buy_amount):
        if self.qty >= 1:
            return self.qty - buy_amount
        return print(f'{self.name} is not currently in stock')

    def restock(self, add_stock_amount):
        self.qty = self.qty + add_stock_amount
        return self.qty

    def delete(self):
        productdb = Product.get_db()
        product_deleted = productdb.delete(self.id)
        if product_deleted:
            print(f'{self.name} successfully removed from database!')
            self.id = None
            self.qty = 0
            return True
        return False

    @staticmethod
    def get_db():
        return gdb(r'~\Documents\code\projects\product_cms\py\product\productdb.json')

    @staticmethod
    def find_by_name(name):
        productdb = Product.get_db()
        for _, product in productdb.db.items():
            if product['name'] == name:
                return product

    @staticmethod
    def find_by_id(id):
        productdb = Product.get_db()
        return productdb.get(id)