import pytest
from product import Product , make_productdb

def setup():
    productdb = make_productdb()
    return productdb

@pytest.fixture()
def productdb():
    productdb = setup()
    return productdb


def test_save():
    p = Product('banana')

    assert p.id is not None
    assert p.name == 'banana'

    p.save()

    assert p.id is not None
    assert p.name == 'banana'
    assert p.save() == True

def test_delete_saved():
    p = Product('banana')

    assert p.id is not None
    assert p.name == 'banana'

    p.save()

    assert p.id is not None
    assert p.name == 'banana'
    assert p.save() == True

    p.delete('banana')

    assert p.id is None
    assert p.name == 'banana'
    assert p.delete == True
