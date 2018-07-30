# NOTE: Before reading this file, make sure you have read pytest_fixtures_in_common_file.py
# Pytest can be used with different scope levels: function, class, module or session.
# The default scope is function. This means that the fixture will be computed
# on each function. The class scope will invoke the fixture once per test class.
# The module scope will invoke the fixture once per module (i.e. file). Finally,
# the session scope invoke the same fixture once for all the modules.
#
# In this file we show the behavior of function and module scope. For it, run:
# $ pytest -s pytest_scope.py
# The result will be the following:
# Training neural network
# .
# Training neural network
# .
# Training neural network
# ..
# =========================== 4 passed in 3.03 seconds ===========================
# As expected, the training function is executed for every function scope, which
# will print "Training neural network" twice and sleep for 2s. Afterwards, one
# training function is executed for the two module scope. That's why there is
# only one print, and the total time is 1s.
#
# More info: https://docs.pytest.org/en/latest/fixture.html#scope-sharing-a-fixture-instance-across-tests-in-a-class-module-or-session
#


def test_train_scope_function1(train_scope_function):
    assert train_scope_function.n_layers == 2


def test_train_scope_function2(train_scope_function):
    assert train_scope_function.n_layers == 2


def test_train_scope_module1(train_scope_module):
    assert train_scope_module.n_layers == 2


def test_train_scope_module2(train_scope_module):
    assert train_scope_module.n_layers == 2
