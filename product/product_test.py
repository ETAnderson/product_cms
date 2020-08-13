import pytest
from product import Product 

def test_save():
    p = Product('banana', 10)

    assert p.id is not None
    assert p.name == 'banana'
    assert p.qty == 10

    assert p.save() == True

    assert p.id is not None
    assert p.name == 'banana'
    assert p.qty == 10

def test_delete_saved():
    p = Product('banana', 10)

    assert p.id is not None
    assert p.name == 'banana'
    assert p.qty == 10

    assert p.save() == True

    assert p.id is not None
    assert p.name == 'banana'
 

    assert p.delete() == True

    assert p.id is None
    assert p.name == 'banana'
    assert p.qty == 0

def test_buy():
    p = Product('banana', 10)

    assert p.id is not None
    assert p.name == 'banana'
    assert p.qty == 10

    assert p.buy(2) == 8

def test_restock():
    p = Product('banana', 10)

    assert p.id is not None
    assert p.name == 'banana'
    assert p.qty == 10

    assert p.restock(10) == 20
    assert p.restock(10) == 30