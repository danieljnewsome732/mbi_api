
def make_response(message=None, status_code=None, exp=None, **kwargs):
    """
    General purpose response creator.

    @param message: use this for the message field; can be overridden by exp.msg if present.
    @param status_code: also can be overridden by exp.
    @param exp: option exception (type=MbiApiError)
    @param **kwargs: anything else to be included in response dict.

    Returns a tuple of dict and http status code.
    Dict has keys 'message' and 'status', and **kwargs (as provided).
    """
    if exp:
        if hasattr(exp, 'status_code'):
            status_code = exp.status_code
        if hasattr(exp, 'msg'):
            message = exp.msg
        if hasattr(exp, 'code'):
            status_code = exp.code
        if hasattr(exp, 'description'):
            message = exp.description
    if status_code is None:
        status_code = 400       # or???

    status = 'success' if 299 >= status_code >= 200 else 'failure'
    if message is None:
        message = 'Ok' if status == 'success' else 'Unknown Error'

    response = dict(message=message, status=status)

    if kwargs:
        response.update(kwargs)

    return response, status_code
