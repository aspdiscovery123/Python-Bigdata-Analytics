
import mathfile

def test_add():
    output=mathfile.add(2,3)
    assert output==5

def test_add_sub():
    output=mathfile.sub(4,3)
    assert output==1

def test_multiply():
    output=mathfile.multiply(2,3)
    assert output==6
