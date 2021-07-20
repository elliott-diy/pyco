#                    _            _
#                   (_)          | |
#         _ __  _ __ ___   ____ _| |_ ___
#        | '_ \| '__| \ \ / / _` | __/ _ \
#        | |_) | |  | |\ V / (_| | ||  __/
#        | .__/|_|  |_| \_/ \__,_|\__\___|
#  ______| |
# |______|_|

"""Private functions and classes for internal use within the package modules."""

from sys import stdout as _stdout
from . import constants as _constants


def _write(code):
    _stdout.write(code)
    _stdout.flush()


def _number_to_code(number):
    return _constants.CSI + str(number) + 'm'


class _Codes(object):
    def __init__(self):
        for member in dir(self):
            if not member.startswith('_') and not callable(getattr(self, member)):
                value = getattr(self, member)
                setattr(self, member, _number_to_code(value))
