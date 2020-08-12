import json
import os
import generic_database as gdb
import uuid

class Product():
    def __init__(self, product_name):
        self.name = product_name
        self.id = uuid.uuid4()

    def save(self):
        productdb = Product.get_db()
        product_saved = productdb.set(self.id, self.name)
        if product_saved:
            print(f'{self.name} successfully added!')
            return True

    def delete(self):
        productdb = Product.get_db()
        product_deleted = productdb.delete(self.id)
        if product_deleted:
            print(f'{self.name} successfully removed from database!')
            self.id = None
            return True
        else:
            return False

    @staticmethod
    def get_db():
        return gdb.GenericDatabase(r'~\Documents\code\projects\product_cms\py\db.json')

