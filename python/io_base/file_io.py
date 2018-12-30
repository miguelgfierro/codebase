def save_line(line, filename):
    """Save a line of text.
    Args:
        line (str): Text.
        filename (str): Name of the file.
    Examples:
        >>> save_line("hello world!", "file.txt")
    """
    with open(filename, "w") as f:
        f.write(line)


def read_line(filename):
    """Read a line of text.
    Args:
        filename (str): Name of the file.
    Returns:
        str: Text.
    Examples:
        >>> read_line("share/data1.txt")
        'I like to move it, move it'
    """
    with open(filename, "r") as f:
        txt = f.readline()
    return txt


def save_list(alist, filename):
    """Save a list to file.
    Args:
        alist (list): Data.
        filename (str): Name of the file.
    Examples:
        >>> save_list(["a","b","bazinga"], "file.txt")
    """
    with open(filename, "w") as f:
        f.write("\n".join(alist))


def read_list(filename):
    """Read a file and returns a list where each element corresponds to a line
    in the file.
    Args:
        filename (str): Name of the file.
    Returns:
        list: A list of elements.
    Examples:
        >>> read_list("share/data.txt")
        ['I like to move it, move it', 'I like to move it, move it', 'I like to move it, move it', 'Ya like to move it']
    """
    with open(filename, "r") as f:
        lines = [line.strip() for line in f]
    return lines
