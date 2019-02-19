import yaml


def save_file(data, filename, block_style=True):
    """Save a dictionary as a YAML file

    Args: 
        data (dict): A dictionary.
        filename (str): Name of the file.
        block_style (bool): If True, with unnested dictionaries, it saves the data with the block format. If False, 
            it will save an unnested dictionary serialized. If the input dict is nested, it will use the block format.
    
    Examples:
        >>> data = {'name': 'Miguel','surname': 'Gonzalez-Fierro', 1:2,'3':'4'}
        >>> save_file(data, 'file.yaml')
    """
    with open(filename, "w") as f:
        yaml.dump(data, f, default_flow_style=not block_style)


def read_file(filename):
    """Read a YAML file

    Args:
        filename (str): Name of the file.
    
    Returns:
        data (dict): A dictionary.

    Examples:
        >>> data = read_file('share/traj.yaml')
        >>> type(data)
        <class 'dict'>
        >>> json.dumps(data, sort_keys=True)
        '{"trajectory": {"q0": [443, 444], "q1": [205, 206], "t": [0.0416667, 0.0833333]}}'
    """
    with open(filename, "r") as f:
        data = yaml.load(f, yaml.SafeLoader)
    return data

