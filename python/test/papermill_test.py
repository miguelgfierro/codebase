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
    nb = pm.read_notebook(OUTPUT_NOTEBOOK)
    df = nb.dataframe
    assert df.shape[0] == 4
    result = df.loc[df["name"] == "result", "value"].values[0]
    assert result == 15
    check_version = df.loc[df["name"] == "checked_version", "value"].values[0]
    assert check_version is True


def test_notebook_fails():
    with pytest.raises(Exception):
        pm.execute_notebook(
            INPUT_NOTEBOOK, OUTPUT_NOTEBOOK, parameters=dict(version="0.1", integer=10)
        )
