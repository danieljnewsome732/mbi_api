"""Data Transfer Objects for various models and controllers."""
from flask_restplus import Namespace, fields


class MbiDto:
    """ Object for mbi operations."""
    api = Namespace("mbi", description="mbi related operations")

    mbi = api.model("mbi", {
        "mbi": fields.String(
            required=True, description="mbi account code"
        )
    })