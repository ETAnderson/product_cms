import json
import os
import pytest
import product
import generic_database as gdb


def test_save():
    p = Product('banana')

    assert p.id is none
    assert p.name == 'banana'

    p.save()

    assert p.id is not none
    assert p.name == 'banana'


test_save()
