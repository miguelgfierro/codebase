import pytest
import pandas as pd
import numpy as np
from collections import Counter


@pytest.fixture()
def basic_structures():
    data = {'int': 5,
            'yes': True,
            'no': False,
            'float': 0.5,
            'pi': 3.141592653589793238462643383279,
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
    series = pd.Series(l)
    return np_array, df, series


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
    l, _ = complex_structures()
    assert l == [1, 2, 3]
    assert Counter(l) == Counter([2, 1, 3])  # list have same elements
    assert 1 in l
    assert 5 not in l
    assert all(x in l for x in [2, 3])  # sublist in list


def test_dictionaries():
    _, d = complex_structures()
    assert d == {'a': 1, 'b': 2}
    assert 'a' in d
    assert d.items() <= {'a': 1, 'b': 2, 'c': 3}.items()  # subdict in dict
    with pytest.raises(KeyError):
        value = d['c']


def test_pandas():
    _, df, series = numeric_libs()
    df_target = pd.DataFrame({'a': 1, 'b': 2}, index=[0])
    series_target = pd.Series([1, 2, 3])
    pd.testing.assert_frame_equal(df, df_target)
    pd.testing.assert_series_equal(series, series_target)


def test_numpy():
    np_array, *_ = numeric_libs()
    np_target = np.array([1, 2, 3])
    np_target2 = np.array([0.9999, 2, 3])
    assert np.all(np_array == np_target)
    np.testing.assert_array_equal(np_array, np_target)  # same as before
    np.testing.assert_array_almost_equal(np_array, np_target2, decimal=4)


