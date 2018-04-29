

def divide(x, y):
    """First, the try clause (result = x / y) is executed. If no exception 
    occurs, the except clause is skipped and execution of the try statement is 
    finished. If an exception occurs, the rest of the clause is skipped. Then 
    if its type matches the exception named after the except keyword, the 
    except clause is executed. If an exception occurs which does not match the 
    exception named in the except clause, it is passed on to outer try 
    statements; if no handler is found, it is an unhandled exception and 
    execution stops. 
    The else clause is executed if no exception is raise.
    The finally clause is executed always.
    source: https://docs.python.org/3.6/tutorial/errors.html#defining-clean-up-actions
    Examples:
        >>> divide(1,2)
        result is 0.5
        executing finally clause
        >>> divide(1,0)
        division by zero!
        executing finally clause
        >>> divide("1","2")
        Traceback (most recent call last):
            ...
        TypeError: unsupported operand type(s) for /: 'str' and 'str'
    """
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

