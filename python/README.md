# Python Codebase

For Python Docstring, I'm using the [Google Style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

To install the libraries:

    conda env update -n py35 -f conda_py35.yaml

To execute the tests:

    pytest --doctest-modules --continue-on-collection-errors


_Note:_

To handle variable outputs in doctest you need to add at the end of the line `#doctest: +ELLIPSIS`.

#### Configuration

To be able to run the test in [blob_io.py](python/io_base/blob_io.py), add the correct credentials after renaming the template:

    cp share/blob_config_template.json share/blob_config.json
