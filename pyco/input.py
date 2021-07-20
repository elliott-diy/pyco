#  _                   _
# (_)                 | |
#  _ _ __  _ __  _   _| |_
# | | '_ \| '_ \| | | | __|
# | | | | | |_) | |_| | |_
# |_|_| |_| .__/ \__,_|\__|
#         | |
#         |_|

"""Functions to simulate keypress input in the terminal window."""

from ._private import _write
from . import constants as _constants


class CursorKeys:
    @staticmethod
    def up_arrow():
        _write(_constants.CSI + 'A')

    @staticmethod
    def down_arrow():
        _write(_constants.CSI + 'B')

    @staticmethod
    def right_arrow():
        _write(_constants.CSI + 'C')

    @staticmethod
    def left_arrow():
        _write(_constants.CSI + 'D')

    @staticmethod
    def home():
        _write(_constants.CSI + 'H')

    @staticmethod
    def end():
        _write(_constants.CSI + 'F')

    @staticmethod
    def ctrl_up_arrow():
        _write(_constants.CSI + '1;5A')

    @staticmethod
    def ctrl_down_arrow():
        _write(_constants.CSI + '1;5B')

    @staticmethod
    def ctrl_right_arrow():
        _write(_constants.CSI + '1;5C')

    @staticmethod
    def ctrl_left_arrow():
        _write(_constants.CSI + '1;5D')


class FunctionKeys:
    @staticmethod
    def backspace():
        _write('\x7f')

    @staticmethod
    def pause():
        _write('\x1a')

    @staticmethod
    def escape():
        _write('\x1b')

    @staticmethod
    def insert():
        _write(_constants.CSI + '2~')

    @staticmethod
    def delete():
        _write(_constants.CSI + '3~')

    @staticmethod
    def page_up():
        _write(_constants.CSI + '5~')

    @staticmethod
    def page_down():
        _write(_constants.CSI + '6~')

    @staticmethod
    def f1():
        _write(_constants.ESC + 'OP')

    @staticmethod
    def f2():
        _write(_constants.ESC + 'OQ')

    @staticmethod
    def f3():
        _write(_constants.ESC + 'OR')

    @staticmethod
    def f4():
        _write(_constants.ESC + 'OS')

    @staticmethod
    def f5():
        _write(_constants.CSI + '15~')

    @staticmethod
    def f6():
        _write(_constants.CSI + '17~')

    @staticmethod
    def f7():
        _write(_constants.CSI + '18~')

    @staticmethod
    def f8():
        _write(_constants.CSI + '19~')

    @staticmethod
    def f9():
        _write(_constants.CSI + '20~')

    @staticmethod
    def f10():
        _write(_constants.CSI + '21~')

    @staticmethod
    def f11():
        _write(_constants.CSI + '23~')

    @staticmethod
    def f12():
        _write(_constants.CSI + '24~')
