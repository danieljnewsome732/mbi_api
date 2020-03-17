"""Error classes for api returns."""


# pylint: disable=super-init-not-called
class MbiApiError(Exception):
    """Parent class."""


# pylint: disable=super-init-not-called
class MbiApiBadRequest(MbiApiError):
    """Bad data in request or other syntactic error"""

    def __init__(self, msg=None):
        """."""
        self.msg = msg or "Bad Request"
        self.status_code = 400


# pylint: disable=super-init-not-called
class MbiApiNotAuthorized(MbiApiError):
    """Auth exception."""

    def __init__(self):
        """."""
        self.msg = "Unauthorized"
        self.status_code = 401


# pylint: disable=super-init-not-called
class MbiApiObjectNotFound(MbiApiError):
    """Not found exception."""

    def __init__(self, obj_type, **kwargs):
        """."""
        self.msg = f"{obj_type} not found"
        if kwargs:
            msg = [f"{key}={value}" for key, value in kwargs.items()]
            msg = ': ' + ', '.join(msg)
            self.msg += msg
        self.status_code = 404


# pylint: disable=super-init-not-called
class MbiApiObjectConflict(MbiApiError):
    """Object already created excption."""

    def __init__(self, msg):
        """."""
        self.msg = msg
        self.status_code = 409


# pylint: disable=super-init-not-called
class MbiApiUnproccessableData(MbiApiError):
    """User input outside expected input."""

    def __init__(self, msg):
        """."""
        self.msg = msg
        self.status_code = 422
