# Python Codebase

For Python Docstring, I'm using the [Google Style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

To install the libraries:

    conda env update -n py35 -f conda_py35.yaml

To execute the tests:

    pytest --doctest-modules --continue-on-collection-errors
