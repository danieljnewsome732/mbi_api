"""MBI API."""
import os
from logging import getLogger

from flask_restplus import Api, Resource
from flask import Blueprint, url_for

from mbi_api.controllers.mbi_controller import api as mbi_ns

from mbi_api.util.errors import MbiApiError
from mbi_api.util.util import make_response


__version__ = '1.3.0'
blueprint = Blueprint('api', __name__)


class HttpsApi(Api):
    """Customization to serve over HTTPS."""

    @property
    def specs_url(self):
        """Monkey patch for HTTPS."""
        scheme = 'https'
        return url_for(self.endpoint('specs'), _external=True, _scheme=scheme)


if os.environ.get("ENV") == 'local':
    api = Api(
        blueprint,
        title='MBI API Swagger',
        version=__version__,
        description='A swagger doc for MBI API.'
    )
else:
    api = HttpsApi(
        blueprint,
        version=__version__,
        title='MBI API Swagger',
        description='A swagger doc for MBI API.'
    )


@api.route("/version")
class Version(Resource):
    """Version endpoint."""

    def get(self):
        """Return the version info."""
        return {'service': 'mbi-api', 'version': __version__}


api.add_namespace(mbi_ns, path='/mbi')

@api.errorhandler(MbiApiError)
def handle_mbi_api_error(error):
    """Api error handler."""
    return make_response(exp=error)


@api.errorhandler(Exception)
def handle_random_error(error):
    """Log stack trace on unknown exceptions."""
    logger = getLogger('mbi-api')
    logger.exception(f"caught {type(error)} {error})")
    return make_response(exp=error)
