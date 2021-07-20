#  _                   _
# | |                 (_)
# | | ___   __ _  __ _ _ _ __   __ _
# | |/ _ \ / _` |/ _` | | '_ \ / _` |
# | | (_) | (_| | (_| | | | | | (_| |
# |_|\___/ \__, |\__, |_|_| |_|\__, |
#           __/ | __/ |         __/ |
#          |___/ |___/         |___/

"""Logging functions integrated with the `print_message()` and `user_input()` functions."""

import os as _os
from datetime import datetime as _datetime
from pathlib import Path as _Path
from typing import Union as _Union
from .utils import remove_ansi as _remove_ansi

working_dir = _os.path.join(_os.getcwd(), '')
log_path = _os.path.join(working_dir, 'logs', 'log.txt')
enable_message_logging = False
enable_input_logging = False
enable_timestamp = True
timestamp_format = '%Y-%m-%d %H:%M:%S%z'
log_level = 1


class Levels:
    """Log level constants to use in the `set_log_level()` function."""
    NONE = 0
    ERROR = 1
    WARNING = 2
    SUCCESS = 3
    INFO = 4
    ALL = 5


def log(message='', prefix=''):
    """
    Log entries with prefixes into a log file.

    Parameters:\n
        `message` - The message to be logged.\n
        `prefix` - The prefix before the message, and after the timestamp.
    """
    timestamp = f'[{_datetime.now().astimezone().strftime(timestamp_format)}]' if enable_timestamp else ''
    if _os.path.exists(log_path):
        message = _remove_ansi(str(message))
        prefix = _remove_ansi(str(prefix))
        if prefix != '' and prefix[-1] != ' ':
            prefix = prefix + ' '
        with open(log_path, 'a') as log_file:
            log_file.write(f'{timestamp} {prefix}{message}\n')

    elif log_level != 0:
        _os.makedirs(_Path(log_path).parent)
        with open(log_path, 'w') as log_file:
            log_file.write(f"{timestamp} [ERROR] Log file missing or inaccessible. Creating a new one.\n")

        log(message=message, prefix=prefix)


def clear_log():
    """
    Clear the log file to save disk space, if the log file exists.
    The file will still exist with one entry, it will not get deleted.
    """
    if _os.path.exists(log_path):
        timestamp = f'[{_datetime.now().astimezone().strftime(timestamp_format)}]' if enable_timestamp else ''
        with open(log_path, 'w') as logFile:
            logFile.write(f"{timestamp} [INFO] Cleared log file contents\n")


def set_log_level(level: _Union[str, int, Levels]):
    """
    Set the log level.

    Parameters:\n
        `level` - `Levels` constant, `str`, or `int`.\n\n
    `str` Options:\n
        `'NONE'` - Don't log any messages.\n
        `'ERROR'` - Log errors.\n
        `'WARNING'` - Log warnings and errors.\n
        `'SUCCESS'` - Log successes, warnings, and errors.\n
        `'INFO'` - Log info, successes, warnings, and errors.\n
        `'ALL'` - Log everything.\n
    `int` Options:\n\n
        `0` - Don't log any messages.\n
        `1` - Log errors.\n
        `2` - Log warnings and errors.\n
        `3` - Log successes, warnings, and errors.\n
        `4` - Log info, successes, warnings, and errors.\n
        `5` - Log everything.\n
    """
    global log_level
    global Levels
    if type(level) == str:
        levels = {
            'NONE': 0,
            'ERROR': 1,
            'WARNING': 2,
            'SUCCESS': 3,
            'INFO': 4,
            'ALL': 5
        }
        log_level = levels.get(level.upper(), 1)

    elif type(level) == int or type(level) == Levels:
        log_level = level
