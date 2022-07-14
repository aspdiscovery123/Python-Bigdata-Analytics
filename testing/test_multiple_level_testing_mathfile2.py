
import mathfile
import pytest

@pytest.mark.parametrize('a,b,result',
                         [(5,6,11),
                           (2.5,6.5,9.0),
                           ("hello","testing","hellotesting")
                          ]
                        )
def test_add(a,b,result):
    assert mathfile.add(a,b) == result
