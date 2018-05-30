# Python Codebase

For Python Docstring, I'm using the [Google Style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

To install the libraries:

    conda env update -n py35 -f conda_py35.yaml


## Configuration

To be able to run the test in [blob_io.py](python/io_base/blob_io.py), add the correct credentials after renaming the template:

    cp share/blob_config_template.json share/blob_config.json

## Tests

To execute the tests:

    pytest --doctest-modules --continue-on-collection-errors

_Note:_

To handle variable outputs in doctest you need to add at the end of the line `#doctest: +ELLIPSIS`.

To execute coverage and see the report:

    coverage run playground.py
    coverage report
    
To see more details on the result, the following command will generate a web where the coverage details can be examined line by line:

    coverage html
    

