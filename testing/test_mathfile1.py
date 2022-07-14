
import mathfile
import pytest
@pytest.mark.number
def test_add():
    output=mathfile.add(2,3)
    assert output==5
@pytest.mark.number
def test_add_sub():
    output=mathfile.sub(4,3)
    assert output==1
@pytest.mark.number
def test_multiply():
    output=mathfile.multiply(2,3)
    assert output==6
@pytest.mark.string
def test_add1():
    output=mathfile.add('Hello',' world')
    assert output=='Hello world'
