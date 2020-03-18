"""MBI API."""
import sys
import logging
import os

from flask import Flask
from flask_cors import CORS
from mbi_api.config import config_by_name


def create_app(config_name="dev"):
    """Generate a new flask app for mbi_api."""
    app = Flask("mbi-api")
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(config_by_name[config_name])

    def reraiser(e, *args):
        # make handle_exception work
        # see https://github.com/noirbizarre/flask-restplus/issues/314
        raise e
    app.handle_exception = reraiser

    init_logging(app)

    return app


def init_logging(app):
    """Initialize loggging for app."""
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter(app.config['LOG_FORMAT']))
    app.logger.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(handler)
    app.logger.debug(f'logger name={app.logger.name} level={app.config["LOG_LEVEL"]}')
    logging.getLogger('flask_cors').level = logging.DEBUG


if __name__ == '__main__':
    mbi_app = create_app()
    mbi_app.run(debug=True)
