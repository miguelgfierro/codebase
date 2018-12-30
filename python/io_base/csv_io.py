import csv


def save_file(data, filename):
    """Save data as csv. 
    Args:
        data (list of lists): Data to save.
        filename (str): Name of the file.
    Examples:
        >>> data = np.ones(5)
        >>> save_file(data, 'file.csv')
    """
    pass


def read_file(filename):
    """Read a csv file into a list of lists.
    Args:
        filename (str): Name of the file.
    Returns:
        data (list of lists): Data to read.
    Examples:
        >>> read_file('share/traj.csv')
        [['0.0416667', '443', '205'], ['0.0833333', '444', '206']]
    """
    with open(filename, newline="") as f:
        reader = csv.reader(f, delimiter=",")
        llist = [row for row in reader]
    return llist
