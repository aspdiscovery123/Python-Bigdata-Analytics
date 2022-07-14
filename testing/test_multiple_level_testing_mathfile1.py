
import mathfile
import pytest

def test_add():
    output=mathfile.add(2,3)
    assert output==5
    assert mathfile.add(2.5,6.5)==9.0
    assert mathfile.add('hello',' testing')=='hello testing'
