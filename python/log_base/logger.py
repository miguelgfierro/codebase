import os
import logging
import logging.config
import yaml


def get_debug_level(debug_level):
    """
    Transform debug level from string to logging flags
    :param debug_level: debug level as string
    :return: debug level as logging flag
    """
    if debug_level == 'INFO':
        return logging.INFO
    elif debug_level == 'DEBUG':
        return logging.DEBUG
    elif debug_level == 'WARNING':
        return logging.WARNING
    elif debug_level == 'ERROR':
        return logging.ERROR
    elif debug_level == 'CRITICAL':
        return logging.CRITICAL
    else:
        return None


def setup_logger(debug_level='ERROR', config_file=''):
    """
    Setup logging configuration.
    :param debug_level: debug level as string
    :param config_file: yaml configuration file
    :return logging object
    """

    level = get_debug_level(debug_level)

    # Get environment debug level if it is defined (overwrite level in code)
    env_debug_level='DEBUG_LEVEL'
    env_level = os.getenv(env_debug_level, None)
    if env_level and get_debug_level(env_level) is not None:
        level = get_debug_level(env_level)

    # Get logger
    log = logging.getLogger()
    log.setLevel(level)

    # Format logger
    if os.path.exists(config_file):
        with open(config_file, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        console = logging.StreamHandler()
        format_str = '%(asctime)s -- %(filename)s:%(lineno)s -- %(levelname)s: %(message)s'
        console.setFormatter(logging.Formatter(format_str))
        log.addHandler(console)

    return log


if __name__ == "__main__":
    """
    Showcase of 3 methods of setting up the logger: via console,
    via yaml file and via environment variable
    """
    execute_example = 1

    if execute_example == 1:
        # Example no config file
        print("Example of logger")
        log = setup_logger(debug_level='DEBUG')
        log.debug("Debug log_base")
    elif execute_example == 2:
        # Example config file
        print("Example of logger configured via yaml file")
        log = setup_logger(debug_level='INFO', config_file='logging.yaml')
        log.info("Info log_base")
        log.error("Error log_base")
    elif execute_example == 3:
        print("Example of logger with environment variable")
        os.environ['DEBUG_LEVEL'] = "DEBUG"
        log = setup_logger(debug_level='INFO')
        log.debug("Debug log_base")
        log.error("Error log_base")

