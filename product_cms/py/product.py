import json
import os
import generic_database as gdb

def make_productdb():
    productdb = gdb.GenericDatabase('')
    return productdb

def first_three(str):
	return str[:3] if len(str) > 3 else str

def assign_product_id(product_name):
    product_id = first_three(product_name.strip().lower())
    return product_id


class Product():
    def __init__(self, product_name):
        self.name = product_name
        self.id = assign_product_id(product_name)

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


