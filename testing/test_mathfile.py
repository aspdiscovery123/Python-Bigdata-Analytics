
import mathfile

def test_add():
    output=mathfile.add(2,3)
    assert output==5

def test_sub():
    output=mathfile.sub(4,3)
    assert output==1

def tst_multiply():
    output=mathfile.multiply(2,3)
    assert output==6
