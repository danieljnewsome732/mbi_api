""" Controller tests """

def test_methods_not_allowed_patch(test_app):
    """Test put to patch endpoints not allowed."""
    resp = test_app.patch("/mbi/")
    assert resp.status == "405 METHOD NOT ALLOWED"
    assert resp.json == {
        'status': 'failure',
        'message': 'The method is not allowed for the requested URL.'
    }
