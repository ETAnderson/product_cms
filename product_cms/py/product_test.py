from product import Product , make_productdb

productdb = make_productdb()

def test_save():
    p = Product('banana')

    assert p.id is None
    assert p.name == 'banana'

    p.save()

    assert p.id is not None
    assert p.name == 'banana'
    assert p.save() == True

def test_delete_saved():
    p = Product('banana')

    assert p.id is None
    assert p.name == 'banana'

    p.save()

    assert p.id is not None
    assert p.name == 'banana'
    assert p.save() == True

    p.delete('banana')

    assert p.id is None
    assert p.name == 'banana'
    assert p.delete == True
    
