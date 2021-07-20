#  _                      _             _
# | |                    (_)           | |
# | |_ ___ _ __ _ __ ___  _ _ __   __ _| |
# | __/ _ \ '__| '_ ` _ \| | '_ \ / _` | |
# | ||  __/ |  | | | | | | | | | | (_| | |
#  \__\___|_|  |_| |_| |_|_|_| |_|\__,_|_|

"""Functions for interacting with and modifying the terminal window."""

import os as _os
from ._private import _write
from . import constants as _constants


def clear_screen(mode = 2):
    """
    Clear the terminal window.\n
    Note: Modes `2` and `3` may not work as expected on Windows.

    Parameters:\n
        `mode` - Which text relative to the cursor to clear.\n
    Options:\n
        `0` - Clear all text from the cursor to the end of the screen.\n
        `1` - Clear all text from the cursor to the beginning of the screen.\n
        `2` - Clear all text.\n
        `3` - Clear all text and delete all lines saved in scrollback buffer.
    """
    _write(_constants.CSI + str(mode) + 'J')


def clear_line(mode = 2):
    """
    Clear text on the current line. Cursor position does not change.

    Parameters:\n
        `mode` - Which text relative to the cursor to clear.\n
    Options:\n
        `0` - Clear all text from the cursor to the end of the line.\n
        `1` - Clear all text from the cursor to the beginning of the line.\n
        `2` - Clear the entire line.
    """
    _write(_constants.CSI + str(mode) + 'K')


def scroll_up(n = 1):
    """Move the text up `n` number of lines."""
    _write(_constants.CSI + str(n) + 'S')


def scroll_down(n = 1):
    """Move the text down `n` number of lines."""
    _write(_constants.CSI + str(n) + 'T')


def set_window_title(title: str):
    """Set the terminal window title."""
    _write(_constants.OSC + '0;' + str(title) + _constants.ST)


def get_size(fallback: tuple = (80, 24)) -> _os.terminal_size:
    """Get the width and height of the terminal window."""
    from shutil import get_terminal_size
    return get_terminal_size(fallback=fallback)


def width_80():
    """Set the terminal window width to `80` columns."""
    _write(_constants.CSI + '?3l')


def width_132():
    """Set the terminal window width to `132` columns."""
    _write(_constants.CSI + '?3h')


def bell():
    """Play a sound."""
    _write(_constants.BEL)


def main_screen_buffer():
    """Switch to main screen buffer."""
    _write(_constants.CSI + '?1049l')


def alt_screen_buffer():
    """Switch to new alternate screen buffer."""
    _write(_constants.CSI + '?1049h')


def reset_all():
    """Reset all terminal settings to their default values."""
    _write(_constants.CSI + '!p')
