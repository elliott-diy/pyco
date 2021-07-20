#            _
#           | |
#   ___ ___ | | ___  _ __
#  / __/ _ \| |/ _ \| '__|
# | (_| (_) | | (_) | |
#  \___\___/|_|\___/|_|

"""ANSI escape codes for color and style."""

from ._private import _write, _Codes
from . import constants as _constants


class Fore(_Codes):
    """ANSI escape codes to set terminal text foreground color."""
    BLACK           = 30
    RED             = 31
    GREEN           = 32
    YELLOW          = 33
    BLUE            = 34
    MAGENTA         = 35
    CYAN            = 36
    WHITE           = 37
    DEFAULT         = 39
    BRIGHT_BLACK    = 90
    BRIGHT_RED      = 91
    BRIGHT_GREEN    = 92
    BRIGHT_YELLOW   = 93
    BRIGHT_BLUE     = 94
    BRIGHT_MAGENTA  = 95
    BRIGHT_CYAN     = 96
    BRIGHT_WHITE    = 97

    @staticmethod
    def eight_bit(n) -> str:
        """
        Range of colors from 0 to 255.

        Parameters:\n
            `n` - Number corresponding to a color.\n
        Options:\n
            `0`-`7` - Normal colors.\n
            `8`-`15` - Bright colors.\n
            `16`-`231` - 216 different colors.\n
            `232`-`255` - Grayscale from black to white in 24 steps.
        """
        return _constants.CSI + '38;5;' + str(n) + 'm'

    EightBit = eight_bit

    @staticmethod
    def twenty_four_bit(value: str) -> str:
        """Set color from an RGB or HEX value."""
        try:
            if type(value) == str:
                value = tuple(int(value.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

        except ValueError:
            raise Exception(f"Invalid HEX value '{value}'")

        (r, g, b) = value
        return _constants.CSI + '38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'

    TwentyFourBit = twenty_four_bit
    RGB = twenty_four_bit
    rgb = twenty_four_bit
    HEX = twenty_four_bit
    hex = twenty_four_bit


class Back(_Codes):
    """ANSI escape codes to set terminal text background color."""
    BLACK           = 40
    RED             = 41
    GREEN           = 42
    YELLOW          = 43
    BLUE            = 44
    MAGENTA         = 45
    CYAN            = 46
    WHITE           = 47
    DEFAULT         = 49
    BRIGHT_BLACK    = 100
    BRIGHT_RED      = 101
    BRIGHT_GREEN    = 102
    BRIGHT_YELLOW   = 103
    BRIGHT_BLUE     = 104
    BRIGHT_MAGENTA  = 105
    BRIGHT_CYAN     = 106
    BRIGHT_WHITE    = 107

    @staticmethod
    def eight_bit(n) -> str:
        """
        Range of colors from 0 to 255.

        Parameters:\n
            `n` - Number corresponding to a color.\n
        Options:\n
            `0`-`7` - Normal colors.\n
            `8`-`15` - Bright colors.\n
            `16`-`231` - 216 different colors.\n
            `232`-`255` - Grayscale from black to white in 24 steps.
        """
        return _constants.CSI + '48;5;' + str(n) + 'm'

    EightBit = eight_bit

    @staticmethod
    def twenty_four_bit(value: str) -> str:
        """Set color from an RGB or HEX value."""
        try:
            if type(value) == str and value.startswith('#'):
                value = tuple(int(value.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4))

        except ValueError:
            raise Exception(f"Invalid HEX value '{value}'")

        (r, g, b) = value
        return _constants.CSI + '48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'

    TwentyFourBit = twenty_four_bit
    RGB = twenty_four_bit
    rgb = twenty_four_bit
    HEX = twenty_four_bit
    hex = twenty_four_bit


class Style(_Codes):
    """ANSI escape codes to set terminal text style."""
    RESET               = 0
    BOLD                = 1
    DIM                 = 2
    ITALIC              = 3
    UNDERLINE           = 4
    SLOW_BLINK          = 5
    FAST_BLINK          = 6
    INVERT              = 7
    STRIKE              = 9
    DOUBLE_UNDERLINE    = 21
    NORMAL              = 22
    NO_UNDERLINE        = 24
    NO_INVERT           = 27


class Screen:
    @staticmethod
    def screen_color(i, r, g, b):
        """
        Change the palette color of the terminal window.

        Paramters:\n
            `i` - Color palette index.\n
            `r`, `g`, `b` - Hexadecimal RGB values between `0` and `ff`.
        """
        _write(_constants.OSC + '4;' + str(i) + ';rgb:' + str(r) + '/' + str(g) + '/' + str(b) + _constants.ESC)


Fore = Fore()
Back = Back()
Style = Style()
fore = Fore
back = Back
style = Style
fg = Fore
bg = Back
fx = Style

ERROR = Fore.BRIGHT_RED
WARNING = Fore.BRIGHT_YELLOW
SUCCESS = Fore.BRIGHT_GREEN
INFO = Fore.WHITE
DEFAULT_MESSAGE_COLOR = Fore.WHITE
DEFAULT_PREFIX_COLOR = Fore.WHITE
DEFAULT_INPUT_COLOR = Fore.WHITE
RESET = Style.RESET
AUTO = None
