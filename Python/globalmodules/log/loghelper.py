import logging
import datetime
import configparser
import json

def log_action(func):
    """
    Decorator used for general logging.
    """
    config_object=bootstrap_config('config.ini')
    str_appname=config_object['application']['name']
    logger=logging.getLogger(str_appname)
    logger.setLevel(logging.INFO)
    setup_local_logging(logger, str_appname)

    def wrapper(*args, **kwargs):
        results=func(*args, *kwargs)
        logrecord={"action":func.__name__, "Timestamp":str(datetime.datetime.utcnow()), "Results":str(results)}
        logger.info(json.dumps(logrecord))
        return results

    return wrapper

def bootstrap_config(strconfigpath):
    """
    Setup configuration object to be used later.
    """
    config = configparser.ConfigParser()
    try:
        config.read(strconfigpath)
    except IOError:
        raise

    return config

def setup_local_logging(logger, strappname):
    """
    Sets up a file if there is not one.
    """
    if logger.hasHandlers():
        pass
    else:
        try:
            logfile=logging.FileHandler(strappname+'log.log')
            logger.addHandler(logfile)
        except IOError:
            with open(strappname+'log.log', 'w+') as logfile:
                pass
            logfile = logging.FileHandler(strappname + 'log.log')
            logger.addHandler(logfile)

