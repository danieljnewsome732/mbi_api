""" """
from mbi_api.services.mbi_service import create_mbi, validate_mbi
    

def test_get_mbi_create(mocker):
    """Test swipes are succesfully returned."""
    mbi = create_mbi()
    assert len(mbi) == 13


def test_get_mbi_validate_positive(mocker):
    """Test swipes are succesfully returned."""
    mbi = validate_mbi({"mbi": "Garbage"})
    assert mbi == None


def test_get_mbi_validate_negative(mocker):
    """Test swipes are succesfully returned."""
    mbi = validate_mbi({"mbi": "6U10-VM9-JN53"})
    assert mbi == True
