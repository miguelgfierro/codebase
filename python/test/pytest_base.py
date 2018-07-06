import pytest
import pandas as pd
import numpy as np


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


@pytest.fixture()
def complex_structures():
    my_list = [1, 2, 3]
    my_dict = {'a': 1, 'b': 2}
    return my_list, my_dict


@pytest.fixture()
def numeric_libs():
    l, d = complex_structures()
    np_array = np.array(l)
    df = pd.DataFrame(d, index=[0])
    return np_array, df


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
    assert struct['int'] > 3
    assert struct['int'] >= 5
    assert struct['int'] < 10
    assert struct['int'] <= 5


def test_lists():
    pass


def test_dictionaries():
    pass


def test_pandas():
    pass


def test_numpy():
    pass


