import os
import logging
import logging.config
import yaml


def get_debug_level(debug_level):
    if debug_level=='INFO':
        return logging.INFO
    elif debug_level=='DEBUG':
        return logging.DEBUG
    elif debug_level=='WARNING':
        return logging.WARNING
    elif debug_level=='ERROR':
        return logging.ERROR
    elif debug_level=='CRITICAL':
        return logging.CRITICAL
    else:
        return None


def setup_logger(path='', debug_level='ERROR'):
    """
    Setup logging configuration
    """

    level = get_debug_level(debug_level)

    # Get environment debug level if it is defined (overwrite level in code)
    env_debug_level='DEBUG_LEVEL'
    env_level = os.getenv(env_debug_level, None)
    if env_level and get_debug_level(env_level) is not None:
        level = get_debug_level(env_level)

    # Get logger
    logger = logging.getLogger()
    logger.setLevel(level)

    # Format logger
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        console = logging.StreamHandler()
        format_str = '%(asctime)s -- %(filename)s:%(lineno)s -- %(levelname)s: %(message)s'
        console.setFormatter(logging.Formatter(format_str))
        logger.addHandler(console)

    return logger



def basic_logger():
    """
    Logger with default configuration
    """
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger


def formatted_logger():
    """
    Logger with formatted output
    """
    logger = logging.getLogger(__name__)
    console = logging.StreamHandler()
    format_str = '%(asctime)s -- %(filename)s:%(lineno)s -- %(levelname)s: %(message)s'
    console.setFormatter(logging.Formatter(format_str))
    logger.addHandler(console)
    logger.setLevel(logging.INFO)

    return logger


def log_something(logger):
    logger.info("Info log")
    logger.debug("Debug log")
    logger.error("Error log")
    logger.warning("Warning log")

if __name__ == "__main__":

    # Example no config file
    print("Example of formatted logger")
    logger_formatted = setup_logger(debug_level='DEBUG')
    log_something(logger_formatted)

    # Example config file
    print("Example of logger configured via yaml file")
    logger_yaml = setup_logger(path='logging.yaml', debug_level='INFO')
    log_something(logger_yaml)
