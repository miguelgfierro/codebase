# NOTE: Before reading this file, make sure you have read pytest_fixtures_in_common_file.py
# and pytest_scope.py
#
# This file shows the teardown behavior. We compute load_dataset once, yield the data in every
# test, and then print that each test has been finished. After all the tests are finished,
# the tear down beavior is shown. We print the statement "Tear down the fixture, with data: ".
# Note that this statement comes after the yield.
#
# To run this file:
# $ pytest -s pytest_teardown.py
# ============================= test session starts ==============================
# pytest_teardown.py Finished test_teardown1
# .Finished test_teardown2
# .Finished test_teardown3
# .Tear down the fixture, with data: ['0.0416667 443 205', '0.0833333 444 206', '0.125 445 205', '0.166667 444 204']
# =========================== 3 passed in 0.05 seconds ===========================
#


def test_teardown1(load_dataset):
    assert len(load_dataset) == 4
    print("Finished test_teardown1")


def test_teardown2(load_dataset):
    assert len(load_dataset) == 4
    print("Finished test_teardown2")


def test_teardown3(load_dataset):
    assert len(load_dataset) == 4
    print("Finished test_teardown3")
