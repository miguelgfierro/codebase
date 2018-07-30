# This file use the common fixtures defined in the file conftest.py.
# There is no need to import this file, pytest manage this by default.


def test_unit_create_nn(nn5):
    assert nn5.name == "NN"
    assert nn5.n_layers == 5
    assert nn5.model is None
