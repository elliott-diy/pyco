#  _            _
# | |          | |
# | |_ _____  _| |_
# | __/ _ \ \/ / __|
# | ||  __/>  <| |_
#  \__\___/_/\_\\__|

"""Functions for interacting with and modifying terminal text."""

from ._private import _write
from . import constants as _constants


def insert_char(n = 1):
    """Insert `n` spaces starting at the current cursor position."""
    _write(_constants.CSI + str(n) + '@')


def delete_char(n = 1):
    """Delete `n` characters starting at the current cursor position."""
    _write(_constants.CSI + str(n) + 'P')


def erase_char(n = 1):
    """Erase `n` characters starting at the current cursor position by overwriting them with a space character."""
    _write(_constants.CSI + str(n) + 'X')


def insert_line(n = 1):
    """Insert `n` lines starting at the current cursor position."""
    _write(_constants.CSI + str(n) + 'L')


def delete_line(n = 1):
    """Delete `n` lines starting from the cursor row."""
    _write(_constants.CSI + str(n) + 'M')


def char_set_ascii():
    """ASCII character mode (default)."""
    _write(_constants.ESC + '(B')


def char_set_line_drawing():
    """
    DEC line drawing character mode.\n
    When this mode is enabled, ASCII characters are mapped as follows:\n
        `j` - `┘`\n
        `k` - `┐`\n
        `l` - `┌`\n
        `m` - `└`\n
        `n` - `┼`\n
        `q` - `─`\n
        `t` - `├`\n
        `u` - `┤`\n
        `v` - `┴`\n
        `w` - `┬`\n
        `x` - `│`\n
        `a` - `▒`\n
        `f` - `°`\n
        `g` - `±`\n
        `y` - `≤`\n
        `z` - `≥`\n
        `{` - `π`\n
        `}` - `£`\n
        `|` - `≠`\n
        ``` ` ``` - `♦`\n
        ```~``` - `·`\n
    For a detailed description see:\n
    https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#designate-character-set
    """
    _write(_constants.ESC + '(0')
