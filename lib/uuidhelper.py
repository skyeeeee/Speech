# coding=utf8

from uuid import UUID
from uuid import uuid4


def get_uuid(upper=False, HYPHEN=False):
    uuid = str(uuid4())
    if not HYPHEN:
        uuid = uuid.replace('-', '')
    if upper:
        return uuid.upper()
    return uuid
