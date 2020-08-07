import json
import os
import pytest
import product 
import generic_database as gdb


def test_save():
    p = product.Product('banana')

    assert p.name == 'banana'

    p.save()

    assert p.name == 'banana'

productdb = product.make_productdb()
test_save()
