import json
import os
import generic_database as gdb
import uuid

def make_productdb():
    productdb = gdb.GenericDatabase('')
    return productdb


class Product():
    def __init__(self, product_name):
        self.name = product_name
        self.id = uuid.uuid4()

    def save(self):
        product_set = productdb.set('key', 'value')
        if product_set:
            product_saved = productdb.dumpdb()
            if product_saved:
                print(f'{self.name} successfully added!')
                return

    def delete(self, key):
        product_deleted = productdb.delete(key)
        if product_deleted:
            print(f'{key} successfully removed from database!')
            return
        else:
            return False



