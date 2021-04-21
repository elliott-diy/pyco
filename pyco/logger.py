"""Logging functions integrated with the `PrintMessage()` and `UserInput()` functions."""

import os
from datetime import datetime
from pathlib import Path

workingDir = os.path.join(os.getcwd(), '')

class Logger:
    logPath = os.path.join(workingDir, 'logs', 'log.txt')
    enableMessageLogging = True
    enableInputLogging = True
    logLevel = 1

    @staticmethod
    def Log(message = '', prefix = '', prefixBrackets: bool = True, includeTimestamp: bool = True):
        """
        Log entries with prefixes into a log file.

        Parameters:\n
            `message` - The message to be logged.\n
            `prefix` - The prefix before the message, and after the timestamp.
        """
        timestamp = ''
        if includeTimestamp:
            timestamp = f"[{datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}] "
        
        if os.path.exists(Logger.logPath):
            message = str(message)
            prefix = str(prefix)
            if prefixBrackets and not prefix == '':
                prefix = f'[{prefix}] '

            with open(Logger.logPath, 'a') as logFile:
                logFile.write(f'{timestamp}{prefix}{message}\n')

        elif Logger.logLevel != 0:
            os.makedirs(Path(Logger.logPath).parent)
            with open(Logger.logPath, 'w') as logFile:
                logFile.write(f"{timestamp}[ERROR] Log file missing or inaccessible. Creating a new one.\n")

            Logger.Log(message=message, prefix=prefix, prefixBrackets=prefixBrackets, includeTimestamp=includeTimestamp)
                
    log = Log

    @staticmethod
    def SetLogLevel(level):
        """
        Set the log level.

        Parameters:\n
            `level` - `Logger.Levels` constant, `str`, or `int`.\n
        `str` Options:\n
            `'NONE'` - Don't log any messages.\n
            `'ERROR'` - Log errors.\n
            `'WARNING'` - Log warnings and errors.\n
            `'SUCCESS'` - Log successes, warnings, and errors.\n
            `'INFO'` - Log info, successes, warnings, and errors.\n
            `'ALL'` - Log everything.\n
        `int` Options:\n
            `0` - Don't log any messages.\n
            `1` - Log errors.\n
            `2` - Log warnings and errors.\n
            `3` - Log successes, warnings, and errors.\n
            `4` - Log info, successes, warnings, and errors.\n
            `5` - Log everything.\n
        """
        if type(level) == str:
            levels = {
                'NONE': 0,
                'ERROR': 1,
                'WARNING': 2,
                'SUCCESS': 3,
                'INFO': 4,
                'ALL': 5
            }
            Logger.logLevel = levels.get(level.upper(), 1)

        elif type(level) == int or type(level) == Logger.Levels:
            Logger.logLevel = level

    set_log_level = SetLogLevel
    LogLevel = SetLogLevel
    log_level = SetLogLevel
    SetLevel = SetLogLevel
    set_level = SetLogLevel

    @staticmethod
    def ClearLog():
        """
        Clear the log file to save disk space. 
        The file will still exist with one entry, it will not get deleted.
        """
        if os.path.exists(Logger.logPath):
            timestamp = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            with open(Logger.logPath, 'w') as logFile:
                logFile.write(f"[{timestamp}] [INFO] Cleared log file contents\n")

        else:
            Logger.Log()

    clear_log = ClearLog

    @staticmethod
    def Set(messageLogging: bool = True, inputLogging: bool = True):
        """
        Enable or disable messsage logging and input logging.\n
        This function is deprecated and may be removed in a future update. 
        Use `Logger.enableMessageLogging = [True/False]` and `Logger.enableInputLogging = [True/False]` instead

        Parameters:\n
            `messageLogging` - Enable or disable message logging.\n
            `inputLogging` - Enable or disable user input logging.
        """
        Logger.enableMessageLogging = messageLogging
        Logger.enableInputLogging = inputLogging

    class Levels:
        """Log level constants to use in the `Logger.SetLogLevel()` function."""
        NONE = 0
        ERROR = 1
        WARNING = 2
        SUCCESS = 3
        INFO = 4
        ALL = 5

    levels = Levels
    LogLevels = Levels
    log_levels = Levels