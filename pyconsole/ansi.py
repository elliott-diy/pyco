"""
ANSI escape codes for use in terminal output. 
Note: Some escape codes may not be supported in all terminals. 
For more information see: 
https://en.wikipedia.org/wiki/ANSI_escape_code
"""

from sys import stdout
from re import findall
from .utils import getch

ESC = '\x1b'
CSI = ESC + '['
OSC = ESC + ']'
ST = ESC + '\\'
BEL = '\x07'

def _Write(code):
    stdout.write(code)
    stdout.flush()

def _NumberToCode(number):
    return CSI + str(number) + 'm'

class _Codes(object):
    def __init__(self):
        for name in dir(self):
            if not name.startswith('_') and not callable(getattr(self, name)):
                value = getattr(self, name)
                setattr(self, name, _NumberToCode(value))

class Terminal:
    @staticmethod
    def ClearScreen(mode = 2):
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
        _Write(CSI + str(mode) + 'J')

    @staticmethod
    def ClearLine(mode = 2):
        """
        Clear text on the current line. Cursor position does not change.

        Parameters:\n
            `mode` - Which text relative to the cursor to clear.\n
        Options:\n
            `0` - Clear all text from the cursor to the end of the line.\n
            `1` - Clear all text from the cursor to the beginning of the line.\n
            `2` - Clear the entire line.
        """
        _Write(CSI + str(mode) + 'K')

    @staticmethod
    def ScrollUp(n = 1):
        """Move the text up `n` number of lines."""
        _Write(CSI + str(n) + 'S')

    @staticmethod
    def ScrollDown(n = 1):
        """Move the text down `n` number of lines."""
        _Write(CSI + str(n) + 'T')

    @staticmethod
    def SetWindowTitle(title: str):
        """Set the terminal window title."""
        _Write(OSC + '0;' + str(title) + ST)

    @staticmethod
    def Width80():
        """Set the terminal window width to `80` columns."""
        _Write(CSI + '?3l')

    @staticmethod
    def Width132():
        """Set the terminal window width to `132` columns."""
        _Write(CSI + '?3h')

    @staticmethod
    def Bell():
        """Play a sound."""
        _Write(BEL)
    
    @staticmethod
    def MainScreenBuffer():
        """Switch to main screen buffer."""
        _Write(CSI + '?1049l')

    @staticmethod
    def AltScreenBuffer():
        """Switch to new alternate screen buffer."""
        _Write(CSI + '?1049h')

    @staticmethod
    def ResetAll():
        """Reset all terminal settings to their default values."""
        _Write(CSI + '!p')

class Cursor:
    @staticmethod
    def Up(n = 1):
        """Move the cursor up `n` number of characters."""
        _Write(CSI + str(n) + 'A')
    
    @staticmethod
    def Down(n = 1):
        """Move the cursor down `n` number of characters."""
        _Write(CSI + str(n) + 'B')

    @staticmethod
    def Right(n = 1):
        """Move the cursor right `n` number of characters."""
        _Write(CSI + str(n) + 'C')

    @staticmethod
    def Left(n = 1):
        """Move the cursor left `n` number of characters."""
        _Write(CSI + str(n) + 'D')

    @staticmethod
    def LineDown(n = 1):
        """Move the cursor down `n` number of lines."""
        _Write(CSI + str(n) + 'E')

    @staticmethod
    def LineUp(n = 1):
        """Move the cursor up `n` number of lines."""
        _Write(CSI + str(n) + 'F')

    @staticmethod
    def Horizontal(x = 0):
        """Move the cursor to column `x`."""
        _Write(CSI + str(x) + 'G')

    @staticmethod
    def Vertical(y = 0):
        """Move the cursor to row `y`."""
        _Write(CSI + str(y) + 'd')

    @staticmethod
    def SetPosition(x = 0, y = 0):
        """Move the cursor to column `x` and line `y`."""
        _Write(CSI + str(x) + ';' + str(y) + 'H')

    @staticmethod
    def GetPosition():
        """
        Get the current cursor position.
        Returns a tuple `(x, y)`.
        """
        _Write(CSI + '6n')
        pos = ''
        while len(pos) == 0 or pos[-1] != 'R':
            pos += str(getch(), 'utf-8') #stdin.read(1)

        x = int(findall(r'\[([0-9]+);', pos)[0])
        y = int(findall(r';([0-9]+)R', pos)[0])
        return (x, y)

    @staticmethod
    def SavePosition():
        """Save the current cursor position in memory to restore later."""
        _Write(CSI + 's')

    @staticmethod
    def RestorePosition():
        """
        Restore the cursor position to the last saved position.
        Defaults to position `0`, `0` if no position was saved.
        """
        _Write(CSI + 'u')

    @staticmethod
    def Show():
        """Make the terminal cursor visible."""
        _Write(CSI + '?25h')

    @staticmethod
    def Hide():
        """Make the terminal cursor invisible."""
        _Write(CSI + '?25l')

    @staticmethod
    def EnableBlink():
        """Make the terminal cursor start blinking."""
        _Write(CSI + '?12h')

    @staticmethod
    def DisableBlink():
        """Make the terminal cursor stop blinking."""
        _Write(CSI + '?12l')

class Color(_Codes):
    class Foreground(_Codes):
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
        def EightBit(n):
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
            return CSI + '38;5;' + str(n) + 'm'

        @staticmethod
        def TwentyFourBit(r, g, b):
            """Set color from an RGB value."""
            return CSI + '38;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'

    class Background(_Codes):
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
        def EightBit(n):
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
            return CSI + '48;5;' + str(n) + 'm'

        @staticmethod
        def TwentyFourBit(r, g, b):
            """Set color from an RGB value."""
            return CSI + '48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm'

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
        def ScreenColor(i, r, g, b):
            """
            Change the palette color of the terminal window.

            Paramters:\n
                `i` - Color palette index, `0` is Text, `1` is Background.\n
                `r`, `g`, `b` - Hexadecimal RGB values between `0` and `ff`.
            """
            _Write(OSC + '4;' + str(i) + ';rgb:' + str(r) + '/' + str(g) + '/' + str(b) + ESC)

    class Fore(Foreground, _Codes):
        """ANSI escape codes to set terminal text foreground color."""
        pass

    class Back(Background, _Codes):
        """ANSI escape codes to set terminal text background color."""
        pass
    
    ERROR = Foreground().BRIGHT_RED
    WARNING = Foreground().BRIGHT_YELLOW
    SUCCESS = Foreground().BRIGHT_GREEN
    INFO = Foreground().WHITE
    DEFAULT_MESSAGE_COLOR = Foreground().WHITE
    DEFAULT_PREFIX_COLOR = Foreground().WHITE
    RESET = Style().RESET
    AUTO = None

class Text:
    @staticmethod
    def InsertChar(n = 1):
        """Insert `n` spaces starting at the current cursor position."""
        _Write(CSI + str(n) + '@')
    
    @staticmethod
    def DeleteChar(n = 1):
        """Delete `n` characters starting at the current cursor position."""
        _Write(CSI + str(n) + 'P')
    
    @staticmethod
    def EraseChar(n = 1):
        """Erase `n` characters starting at the current cursor position by overwriting them with a space character."""
        _Write(CSI + str(n) + 'X')

    @staticmethod
    def InsertLine(n = 1):
        """Insert `n` lines starting at the current cursor position."""
        _Write(CSI + str(n) + 'L')

    @staticmethod
    def DeleteLine(n = 1):
        """Delete `n` lines starting from the cursor row."""
        _Write(CSI + str(n) + 'M')

    @staticmethod
    def CharSetASCII():
        """ASCII character mode (default)."""
        _Write(ESC + '(B')

    @staticmethod
    def CharSetLineDrawing():
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
            `x` - `│`\n\n
        For a detailed description see:\n
        https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences#designate-character-set
        """
        _Write(ESC + '(0')

class Input:
    class CursorKeys:
        @staticmethod
        def UpArrow():
            _Write(CSI + 'A')

        @staticmethod
        def DownArrow():
            _Write(CSI + 'B')

        @staticmethod
        def RightArrow():
            _Write(CSI + 'C')

        @staticmethod
        def LeftArrow():
            _Write(CSI + 'D')

        @staticmethod
        def Home():
            _Write(CSI + 'H')

        @staticmethod
        def End():
            _Write(CSI + 'F')

        @staticmethod
        def CtrlUpArrow():
            _Write(CSI + '1;5A')

        @staticmethod
        def CtrlDownArrow():
            _Write(CSI + '1;5B')

        @staticmethod
        def CtrlRightArrow():
            _Write(CSI + '1;5C')

        @staticmethod
        def CtrlLeftArrow():
            _Write(CSI + '1;5D')

    class FunctionKeys:
        @staticmethod
        def Backspace():
            _Write('\x7f')

        @staticmethod
        def Pause():
            _Write('\x1a')

        @staticmethod
        def Escape():
            _Write('\x1b')

        @staticmethod
        def Insert():
            _Write(CSI + '2~')

        @staticmethod
        def Delete():
            _Write(CSI + '3~')

        @staticmethod
        def PageUp():
            _Write(CSI + '5~')

        @staticmethod
        def PageDown():
            _Write(CSI + '6~')

        @staticmethod
        def F1():
            _Write(ESC + 'OP')

        @staticmethod
        def F2():
            _Write(ESC + 'OQ')

        @staticmethod
        def F3():
            _Write(ESC + 'OR')

        @staticmethod
        def F4():
            _Write(ESC + 'OS')

        @staticmethod
        def F5():
            _Write(CSI + '15~')

        @staticmethod
        def F6():
            _Write(CSI + '17~')

        @staticmethod
        def F7():
            _Write(CSI + '18~')

        @staticmethod
        def F8():
            _Write(CSI + '19~')

        @staticmethod
        def F9():
            _Write(CSI + '20~')

        @staticmethod
        def F10():
            _Write(CSI + '21~')

        @staticmethod
        def F11():
            _Write(CSI + '23~')

        @staticmethod
        def F12():
            _Write(CSI + '24~')

Color.Foreground = Color.Foreground()
Color.Background = Color.Background()
Color.Fore = Color.Fore()
Color.Back = Color.Back()
Color.Style = Color.Style()
Foreground = Color.Foreground
Background = Color.Background
Fore = Color.Fore
Back = Color.Back
Style = Color.Style
Screen = Color.Screen