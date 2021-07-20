#              _       _ _
#             (_)     (_) |
#              _ _ __  _| |_
#             | | '_ \| | __|
#             | | | | | | |_
#             |_|_| |_|_|\__|
#  ______ ______          ______ ______
# |______|______|        |______|______|

"""
Colored console printing and input, ANSI escape codes, and logging functions.\n
Version: 0.8\n
Made by Duplexes and LemonPi314.\n
https://github.com/Duplexes/pyconsole \n
Full documentation at https://duplexes.me/pyco
"""

from .pyco import print_message, user_input, NonBlockingInput
from . import color, constants, cursor, input, logging, prefix, progress, terminal, text, utils

# Failed attempt at cleaning up import namespace.
#
# for module in [color, cursor, input, logging, prefix, progress, terminal, text, utils]:
#     for member in dir(module):
#         try:
#             if member.startswith('_') and not member.startswith('__'):
#                 member = getattr(module, member)
#                 del member
#         except AttributeError:
#             pass

__version__: str = '0.8'
version: str = __version__
