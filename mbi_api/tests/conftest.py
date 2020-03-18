"""Fixtures for testing."""
from io import StringIO, BytesIO
import os

import arrow
import mock
import pandas
import pytest

from mbi_api.app import create_app
from mbi_api import blueprint


@pytest.fixture(scope='module')
def test_app():
    """Generate test app."""
    os.environ['FLASK_ENV'] = 'Testing'
    app = create_app("test")
    app.register_blueprint(blueprint)
    test_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield test_client

    ctx.pop()