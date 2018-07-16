# Python Codebase

For Python Docstring, I'm using the [Google Style](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).

To install the libraries:

    conda env create -n codebase -f conda.yaml

## Configuration

To be able to run the test in [blob_io.py](python/io_base/blob_io.py), add the correct credentials after renaming the template:

    cp share/blob_config_template.json share/blob_config.json

## Tests

To execute the tests:

    pytest --doctest-modules --continue-on-collection-errors

To execute coverage and see the report:

    coverage run playground.py
    coverage report
    
To see more details on the result, the following command will generate a web where the coverage details can be examined line by line:

    coverage html
    

To handle variable outputs in doctest you need to add at the end of the execution line `#doctest: +ELLIPSIS` and substitude the variable output with `...`
An example can be found in the file [timer.py](python/log_base/timer.py).

Original:

    >>> "Time elapsed {}".format(t)
    'Time elapsed 0:00:1.9875734'

With ellipsis:

    >>> "Time elapsed {}".format(t) #doctest: +ELLIPSIS
    'Time elapsed 0:00:...'

To handle [exceptions](https://docs.python.org/2.4/lib/doctest-exceptions.html), you can just add the `Traceback` info, then `...` and then the exception:

    >>> raise ValueError("Something bad happened")
    Traceback (most recent call last):
        ...
    ValueError: "Something bad happened"
