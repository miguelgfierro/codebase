import pytest


@pytest.fixture()
def basic_structures():
    data = {'int':5,
            'yes':True,
            'no':False,
            'float': 0.5,
            'pi':3.141592653589793238462643383279,
            'string': 'Miguel',
            'none': None}
    return data


def test_basic_structures():
    struct = basic_structures()
    assert struct['int'] == 5
    assert struct['yes'] is True
    assert struct['no'] is False
    assert struct['float'] == 0.5
    assert struct['string'] == 'Miguel'
    assert struct['none'] is None


def test_comparing_numbers():
    struct = basic_structures()
    assert struct['pi'] == pytest.approx(3.1415926, 0.0000001)
    assert struct['pi'] != pytest.approx(3.1415926, 0.00000001)

