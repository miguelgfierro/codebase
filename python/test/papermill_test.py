import papermill as pm
import pytest


def test_notebook_runs():
    pm.execute_notebook(
        "papermill_notebook.ipynb",
        "output.ipynb",
        parameters=dict(version=pm.__version__, integer=10),
    )
    nb = pm.read_notebook("output.ipynb")
    df = nb.dataframe
    assert df.shape[0] == 4
    result = df.loc[df["name"] == "result", "value"].values[0]
    assert result == 15
    check_version = df.loc[df["name"] == "checked_version", "value"].values[0]
    assert check_version is True


def test_notebook_fails():
    with pytest.raises(Exception):
        pm.execute_notebook(
            "papermill_notebook.ipynb",
            "output.ipynb",
            parameters=dict(version="0.1", integer=10),
        )
