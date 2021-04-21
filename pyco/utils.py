import os, msvcrt, ctypes
from ctypes import wintypes

class WindowsConsole:
    def __init__(self):
        """Windows calls to enable ANSI escape codes."""
        self.kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
        self.ERROR_INVALID_PARAMETER = 0x0057
        self.ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        self.LPDWORD = ctypes.POINTER(wintypes.DWORD)
        self.kernel32.GetConsoleMode.errcheck = self._check_bool
        self.kernel32.GetConsoleMode.argtypes = (wintypes.HANDLE, self.LPDWORD)
        self.kernel32.SetConsoleMode.errcheck = self._check_bool
        self.kernel32.SetConsoleMode.argtypes = (wintypes.HANDLE, wintypes.DWORD)

    def _check_bool(self, result, func, args):
        if not result:
            raise ctypes.WinError(ctypes.get_last_error())

        return args

    def set_conout_mode(self, new_mode, mask=0xffffffff):
        fdout = os.open('CONOUT$', os.O_RDWR)
        try:
            hout = msvcrt.get_osfhandle(fdout)
            old_mode = wintypes.DWORD()
            self.kernel32.GetConsoleMode(hout, ctypes.byref(old_mode))
            mode = (new_mode & mask) | (old_mode.value & ~mask)
            self.kernel32.SetConsoleMode(hout, mode)
            return old_mode.value
            
        finally:
            os.close(fdout)

    def enable_vt_mode(self):
        """Force Windows terminals to work with ANSI escape codes."""
        mode = mask = self.ENABLE_VIRTUAL_TERMINAL_PROCESSING
        try:
            return self.set_conout_mode(mode, mask)

        except WindowsError as e:
            if e.winerror == self.ERROR_INVALID_PARAMETER:
                raise NotImplementedError
                
            raise

class Getch:
    """
    Gets a single character from standard input.
    Does not echo to the screen.
    """
    def __init__(self):
        try:
            self.impl = self._GetchWindows()

        except ImportError:
            self.impl = self._GetchUnix()

    def __call__(self):
        return self.impl()

    class _GetchUnix:
        def __init__(self):
            import sys, tty

        def __call__(self):
            import sys, tty, termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                char = sys.stdin.read(1)

            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

            return char

    class _GetchWindows:
        def __init__(self):
            import msvcrt

        def __call__(self):
            return msvcrt.getch()

WinConsole = WindowsConsole
WinCon = WindowsConsole
getch = Getch()