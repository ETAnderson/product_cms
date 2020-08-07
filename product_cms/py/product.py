import json
import os
import generic_database as gdb

def make_productdb():
    productdb = gdb.GenericDatabase('')
    return productdb

class Product():
    def __init__(self, product_name):
        self.name = product_name

    def save(self):
        product_set = productdb.set('key', 'value')
        if product_set:
            product_saved = productdb.dumpdb()
            if product_saved:
                print(f'{self.name} successfully added!')


