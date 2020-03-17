"""MBI Controller."""

from flask import request
from flask_restplus import Resource

from mbi_api.util.dto import MbiDto

from mbi_api.util.errors import (
    MbiApiObjectNotFound, MbiApiNotAuthorized
)
from mbi_api.util.util import make_response

from mbi_api.services.mbi_service import create_mbi, validate_mbi

_mbi = MbiDto.mbi
api = MbiDto.api


@api.route('/')
class Mbi(Resource):
    """Class for MBI validate / create."""
    def get(self):
        """Create an MBI."""
        mbi=create_mbi()    
        return mbi, 201

    @api.expect(_mbi, validate=True)
    def post(self):
        """Validate an MBI."""
        if validate_mbi(request.json):
            return make_response('MBI is valid', 200)
        else:
            return make_response('MBI is invalid', 200)