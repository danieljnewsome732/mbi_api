"""Config Handlers."""
import os

# pylint: disable=too-few-public-methods
class Config:
    """Base config class."""

    DEBUG = True
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 3030
    THREADS = 4

    # Use the LOG_LEVEL var if it's present, so that someone trying to debug the service can do `export LOG_LEVEL=DEBUG`
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
    LOG_NAME = "mbi_api"
    LOG_FORMAT = "[%(levelname)s] %(module)s.%(funcName)s.%(lineno)d | %(message)s"

    SECRET_KEY = os.environ.get("SESSION_SECRET")
    PROPAGATE_EXCEPTIONS = False
    ERROR_404_HELP = False


class Production(Config):
    """Production config."""

    DEBUG = False
    THREADS = 8


class Development(Config):
    """Development config."""

class Staging(Config):
    """Development config."""

class Testing(Config):
    """Testing config."""

    TESTING = True
    LOG_LEVEL = "DEBUG"
    WTF_CSRF_ENABLED = False


config_by_name = dict(
    local=Development,
    dev=Development,
    staging=Staging,
    test=Testing,
    prod=Production
)

key = Config.SECRET_KEY
