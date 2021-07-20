#        _   _ _
#       | | (_) |
#  _   _| |_ _| |___
# | | | | __| | / __|
# | |_| | |_| | \__ \
#  \__,_|\__|_|_|___/

"""Utility terminal functions and classes."""

import os as _os
import re as _re

windows = _os.name == 'nt'
if windows:
    import msvcrt as _msvcrt
    import ctypes as _ctypes
    from ctypes import wintypes as _wintypes
else:
    import tty as _tty
    import termios as _termios
    import select as _select
    from sys import stdin as _stdin


def clear_screen_command():
    if windows:
        _os.system('cls')
    else:
        _os.system('clear')


class WindowsConsole:
    def __init__(self):
        """Windows calls to enable ANSI escape codes."""
        self.kernel32 = _ctypes.WinDLL('kernel32', use_last_error=True)
        self.ERROR_INVALID_PARAMETER = 0x0057
        self.ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        self.LPDWORD = _ctypes.POINTER(_wintypes.DWORD)
        self.kernel32.GetConsoleMode.errcheck = self._check_bool
        self.kernel32.GetConsoleMode.argtypes = (_wintypes.HANDLE, self.LPDWORD)
        self.kernel32.SetConsoleMode.errcheck = self._check_bool
        self.kernel32.SetConsoleMode.argtypes = (_wintypes.HANDLE, _wintypes.DWORD)

    def _check_bool(self, result, func, args):
        if not result:
            raise _ctypes.WinError(_ctypes.get_last_error())
        return args

    def set_conout_mode(self, new_mode, mask=0xffffffff):
        fdout = _os.open('CONOUT$', _os.O_RDWR)
        try:
            hout = _msvcrt.get_osfhandle(fdout)
            old_mode = _wintypes.DWORD()
            self.kernel32.GetConsoleMode(hout, _ctypes.byref(old_mode))
            mode = (new_mode & mask) | (old_mode.value & ~mask)
            self.kernel32.SetConsoleMode(hout, mode)
            return old_mode.value
        finally:
            _os.close(fdout)

    def enable_vt_mode(self):
        """Force Windows terminals to work with ANSI escape codes."""
        mode = mask = self.ENABLE_VIRTUAL_TERMINAL_PROCESSING
        try:
            return self.set_conout_mode(mode, mask)
        except WindowsError as exception:
            if exception.winerror == self.ERROR_INVALID_PARAMETER:
                raise NotImplementedError
            raise exception


WindowsConsole = WindowsConsole()
if windows:
    WindowsConsole.enable_vt_mode()


class _getch:
    def __init__(self):
        if windows:
            self.impl = self._getch_windows()
        else:
            self.impl = self._getch_unix()

    def __call__(self):
        return self.impl()

    class _getch_windows:
        def __init__(self):
            pass

        def __call__(self) -> str:
            return _msvcrt.getch().decode('utf-8', errors='replace')

    class _getch_unix:
        def __init__(self):
            self.fd = _stdin.fileno()
            self.old_term = _termios.tcgetattr(self.fd)

        def __call__(self) -> str:
            try:
                _tty.setraw(self.fd)
                char = _stdin.read(1)
            finally:
                _termios.tcsetattr(self.fd, _termios.TCSADRAIN, self.old_term)
            return char


_getch = _getch()


def getch() -> str:
    """Get a single character from standard input."""
    return _getch()


class _kbhit:
    def __init__(self):
        if windows:
            self.impl = self._kbhit_windows()
        else:
            self.impl = self._kbhit_unix()

    def __call__(self):
        return self.impl()

    class _kbhit_windows:
        def __init__(self):
            pass

        def __call__(self) -> bool:
            return _msvcrt.kbhit() == 1

    class _kbhit_unix:
        def __init__(self):
            self.fd = _stdin.fileno()
            self.old_term = _termios.tcgetattr(self.fd)
            self.new_term = _termios.tcgetattr(self.fd)
            self.new_term[3] = (self.new_term[3] & ~_termios.ICANON & ~_termios.ECHO)

        def __call__(self) -> bool:
            _termios.tcsetattr(self.fd, _termios.TCSAFLUSH, self.new_term)
            try:
                dr, dw, de = _select.select([_stdin], [], [], 0)
            finally:
                _termios.tcsetattr(self.fd, _termios.TCSAFLUSH, self.old_term)
            return dr != []


_kbhit = _kbhit()


def kbhit() -> bool:
    """Return `True` if a keypress is available in the buffer."""
    return _kbhit()


def remove_ansi(string):
    """Remove any ANSI escape codes from a string."""
    ansi_escape = _re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', string)
