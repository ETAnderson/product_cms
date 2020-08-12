import pytest
from product import Product 

def test_save():
    p = Product('banana')

    assert p.id is not None
    assert p.name == 'banana'

    assert p.save() == True

    assert p.id is not None
    assert p.name == 'banana'


def test_delete_saved():
    p = Product('banana')

    assert p.id is not None
    assert p.name == 'banana'

    assert p.save() == True

    assert p.id is not None
    assert p.name == 'banana'
 

    assert p.delete() == True

    assert p.id is None
    assert p.name == 'banana'

