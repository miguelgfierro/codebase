import papermill as pm
import pytest

INPUT_NOTEBOOK = "python/test/papermill_notebook.ipynb"
OUTPUT_NOTEBOOK = "output.ipynb"


def test_notebook_runs():
    pm.execute_notebook(
        INPUT_NOTEBOOK,
        OUTPUT_NOTEBOOK,
        parameters=dict(version=pm.__version__, integer=10),
    )
    results = pm.read_notebook(OUTPUT_NOTEBOOK).dataframe.set_index("name")["value"]
    assert results["result"] == 15
    assert results["checked_version"] is True
    assert results["integer"] == 10


def test_notebook_fails():
    with pytest.raises(Exception):
        pm.execute_notebook(
            INPUT_NOTEBOOK, OUTPUT_NOTEBOOK, parameters=dict(version="0.1", integer=10)
        )
