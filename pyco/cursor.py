#   ___ _   _ _ __ ___  ___  _ __
#  / __| | | | '__/ __|/ _ \| '__|
# | (__| |_| | |  \__ \ (_) | |
#  \___|\__,_|_|  |___/\___/|_|

"""Functions to interact with and modify the terminal cursor."""

from re import findall as _findall
from ._private import _write
from . import constants as _constants
from .utils import _getch


def up(n = 1):
    """Move the cursor up `n` number of characters."""
    _write(_constants.CSI + str(n) + 'A')


def down(n = 1):
    """Move the cursor down `n` number of characters."""
    _write(_constants.CSI + str(n) + 'B')


def right(n = 1):
    """Move the cursor right `n` number of characters."""
    _write(_constants.CSI + str(n) + 'C')


def left(n = 1):
    """Move the cursor left `n` number of characters."""
    _write(_constants.CSI + str(n) + 'D')


def line_up(n = 1):
    """Move the cursor up `n` number of lines."""
    _write(_constants.CSI + str(n) + 'F')


def line_down(n = 1):
    """Move the cursor down `n` number of lines."""
    _write(_constants.CSI + str(n) + 'E')


def horizontal(x = 0):
    """Move the cursor to column `x`."""
    _write(_constants.CSI + str(x) + 'G')


def vertical(y = 0):
    """Move the cursor to row `y`."""
    _write(_constants.CSI + str(y) + 'd')


def set_position(x = 0, y = 0):
    """Move the cursor to column `x` and line `y`."""
    _write(_constants.CSI + str(y) + ';' + str(x) + 'H')


def get_position() -> tuple:
    """
    Get the current cursor position.
    Returns a tuple `(x, y)`.
    """
    _write(_constants.CSI + '6n')
    pos = ''
    while len(pos) == 0 or pos[-1] != 'R':
        pos += _getch()

    x = int(_findall(r'\[([0-9]+);', pos)[0])
    y = int(_findall(r';([0-9]+)R', pos)[0])
    return (x, y)


def save_position():
    """Save the current cursor position in memory to restore later."""
    _write(_constants.CSI + 's')


def restore_position():
    """
    Restore the cursor position to the last saved position.
    defaults to position `0`, `0` if no position was saved.
    """
    _write(_constants.CSI + 'u')


def show():
    """Make the terminal cursor visible."""
    _write(_constants.CSI + '?25h')


def hide():
    """Make the terminal cursor invisible."""
    _write(_constants.CSI + '?25l')


def enable_blink():
    """Make the terminal cursor start blinking."""
    _write(_constants.CSI + '?12h')


def disable_blink():
    """Make the terminal cursor stop blinking."""
    _write(_constants.CSI + '?12l')
