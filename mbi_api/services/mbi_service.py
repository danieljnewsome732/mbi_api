"""Token Service."""
import secrets
import hashlib
import random
import string
import re

from datetime import datetime
from dateutil.relativedelta import relativedelta

from passlib.hash import pbkdf2_sha256

from matchbox.queries.error import DocumentDoesNotExists

from mbi_api.util.errors import MbiApiNotAuthorized


def get_random_from_allowed_chars(typeofchar):
    """Get a random char, of a type."""

    mbi_allowed_letters = "ACDEFGHJKMNPQRTUVWXY"

    if typeofchar == 'C':
        return str(random.randint(1,9))
    elif typeofchar == 'A':
        return random.choice(list(mbi_allowed_letters))
    elif typeofchar == 'E':
        return random.choice(list(mbi_allowed_letters)+list(string.digits))
    elif typeofchar == 'N':
        return str(random.randint(0,9))
    else:
        return "-"


def create_mbi():
    """ Defines the MBI format
        Based on https://med.noridianmedicare.com/web/jfa/topics/mbi
        C = 1-9
        A = Alpha (except S,L,O,I,B,Z)
        E = Either
        N = 0-9
    """

    mbi_format =  "CAEN-AEN-AANN" 
    mbi = ''

    for char in mbi_format:
        mbi += get_random_from_allowed_chars(char)

    return mbi
   

def validate_mbi(data):
    """Get an MBI's validity."""

    mbi_regex = r"^[1-9]{1}[^SLOIBZsloibz|^0-9]{1}[^SLOIBZsloibz]{1}[0-9]{1}-?[^SLOIBZsloibz|^0-9]{1}[^SLOIBZsloibz]{1}[0-9]{1}-?[^SLOIBZsloibz|^0-9]{1}[^SLOIBZsloibz|^0-9]{1}[0-9]{1}[0-9]{1}"
    mbi = data['mbi']

    return re.match(mbi_regex, mbi) and len(mbi) == 13
   
