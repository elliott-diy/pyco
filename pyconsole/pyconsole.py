"""
                                       _      
                                      | |     
 _ __  _   _  ___ ___  _ __  ___  ___ | | ___ 
| '_ \| | | |/ __/ _ \| '_ \/ __|/ _ \| |/ _ \
| |_) | |_| | (_| (_) | | | \__ \ (_) | |  __/
| .__/ \__, |\___\___/|_| |_|___/\___/|_|\___|
| |     __/ |                                 
|_|    |___/                                  

Made by Duplexes and LemonPi314
https://github.com/Duplexes/pyconsole
"""

import os, time
from datetime import datetime
from pathlib import Path

# This must be run when the program starts to clear a color bug on Windows consoles
ClearScreen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

clearscreen = ClearScreen
clear_screen = ClearScreen
clear = ClearScreen
cls = ClearScreen

def ClearScreenFunction():
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')

ClearScreenFunc = ClearScreenFunction
clear_screen_function = ClearScreenFunction
clearscreen_func = ClearScreenFunction
clear_screen_func = ClearScreenFunction
clear_func = ClearScreenFunction
cls_func = ClearScreenFunction

# Get the name of the current operating system
osName = os.name

# If the operating system is Windows, clear the console screen to fix the color bug
if osName == 'nt':
    ClearScreen()

# Get the directory containing the project files
workingDir = os.getcwd()
projectDir = Path(workingDir)

# Set the default log file directory
_logPath = os.path.join(projectDir, 'logs', 'log.txt')

# Variables to enable or disable message logging and input logging
_enableMessageLogging = True
_enableInputLogging = True

# Set default log level
_logLevelInt = 3

class Color:
    """
    Color constants as console escape codes.
    """
    Reset = '\u001b[0m'
    Black = '\u001b[30m'
    Red = '\u001b[31m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Magenta =  '\u001b[35m'
    Cyan = '\u001b[36m'
    White = '\u001b[37m'
    BrightBlack = '\u001b[30;1m'
    BrightRed = '\u001b[31;1m'
    BrightGreen = '\u001b[32;1m'
    BrightYellow = '\u001b[33;1m'
    BrightBlue = '\u001b[34;1m'
    BrightMagenta = '\u001b[35;1m'
    BrightCyan = '\u001b[36;1m'
    BrightWhite = '\u001b[37;1m'

color = Color

# Premade tools and functions
def PrintMessage(message: str = '', prefix: str = 'none', messageColor: Color = Color.White, prefixColor: Color = None, colorBrackets: bool = False, forceLog: bool = None, sep: str = ' ', end: str = '\n', flush: bool = False):
    """
    A replacement for `print()` with color and various prefix and logging options. 
    Certain prefixes like `Error` and `Warning` are automatically colored appropriately. 
    You may override the automatic coloring.

    Parameters:\n
    `message` - The message you want to print.\n
    `prefix` - The label before the message.\n
    `messageColor` - The color for the message.\n
    `prefixColor` - The color for the prefix.\n
    `colorBrackets` - Choose whether to color the square brackets surrounding the prefix or not.\n
    `forceLog` - Force the message to be logged regardless of the label.
    """
    log = False
    color = Color.White
    if prefix.lower().find('error') != -1:
        color = Color.BrightRed
        if _logLevelInt >= 1:
            log = True

    elif prefix.lower().find('warning') != -1:
        color = Color.BrightYellow
        if _logLevelInt >= 2:
            log = True

    elif prefix.lower().find('success') != -1:
        color = Color.BrightGreen
        if _logLevelInt >= 3:
            log = True

    elif prefix.lower().find('info') != -1:
        color = Color.White
        if _logLevelInt >= 4:
            log = True

    elif prefix.lower() == 'none':
        prefix = ''
        color = Color.White
        if _logLevelInt == 5:
            log = True

    if prefixColor is None:
        prefixColor = color
        
    if messageColor is None:
        messageColor = Color.White

    if forceLog is not None:
        log = forceLog

    if log:
        Logger.Log(message, prefix)

    if prefix != '':
        if colorBrackets == True:
            print(f'{Color.Reset}{prefixColor}[{prefix}] {Color.Reset}{messageColor}{message}{Color.Reset}', sep=sep, end=end, flush=flush)

        elif colorBrackets == False:
            print(f'{Color.Reset}[{prefixColor}{prefix}{Color.Reset}] {messageColor}{message}{Color.Reset}', sep=sep, end=end, flush=flush)

    elif prefix == '':
        print(Color.Reset + messageColor + message + Color.Reset)

Print = PrintMessage
print_message = PrintMessage
PrintMsg = PrintMessage
print_msg = PrintMessage

def UserInput(prefix: str = '', prefixColor: Color = Color.White, inputColor: Color = Color.White, sep: str = ' ', end: str = '', flush: bool = True):
    """
    A replacement for `input()` with colors.

    Parameters:\n
    `prefix` - The prompt before user's input.\n
    `prefixColor` - The color for the prompt.\n
    `inputColor` - The color for the user's input.
    """
    prefix = str(prefix)
    print(prefixColor + prefix + Color.Reset + inputColor, sep=sep, end=end, flush=flush)
    userInput = input()
    if _enableInputLogging == True:
        Logger.Log(userInput, prefix, False)

    return userInput

Input = UserInput
userinput = UserInput
user_input = UserInput

class ProgressBar:
    def __init__(self, iteration: int = 0, total: int = 100, updateIntervalms: float = 100, prefix: str = '', suffix: str = '', length: int = 100, fill: str = '█', decimals: int = 1, end: str = '\r'):
        """
        Create an instance of this class to create a progress bar in the console using `p = ProgressBar()`. 
        To update the progress bar call `p.Update(counter)` in a loop where `counter` is increased every iteration.

        Parameters:\n
        `iteration` - Current iteration.\n
        `total` - Total iterations.\n
        `prefix` - Prefix string.\n
        `suffix` - Suffix string.\n
        `length` - Character length of bar.\n
        `fill` - Bar fill character.\n
        `decimals` - Positive number of decimals in percent complete.\n
        `end` - End character (e.g. `'\\r'`, `'\\r\\n'`).
        """
        self.iteration = iteration
        self.total = total
        self.updateIntervalms = updateIntervalms
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.decimals = decimals
        self.end = end
        self.lastUpdateTime: time = 0
    
    def Update(self, iteration = None, force = False):
        now = time.time()
        if iteration != None:
            self.iteration = iteration

        if self.updateIntervalms == 0:
            self.updateIntervalms = 1

        if force == False and self.iteration < self.total and (now - self.lastUpdateTime) < (self.updateIntervalms / 1000):
            return
            
        self.lastUpdateTime = now
        ProgressBar._PrintProgressBar(self.iteration, self.total, self.prefix, self.suffix, self.length, self.fill, self.decimals, self.end)
        if self.iteration == self.total:
            print()

    update = Update

    @staticmethod
    def _PrintProgressBar(iteration: int, total: int, prefix: str = '', suffix: str = '', length: int = 100, fill: str = '█', decimals: int = 1, end: str = '\r'):
        percent = ('{0:.' + str(decimals) + 'f}').format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=end)

class Logger:
    @staticmethod
    def Log(message = '', prefix = '', prefixBrackets: bool = True, includeTimestamp: bool = True):
        """
        Log entries with prefixes into a log file.

        Parameters:\n
        `message` - The message to be logged.\n
        `prefix` - The prefix before the message, and after the timestamp.
        """
        if _enableMessageLogging == True:
            timestamp = ''
            if includeTimestamp:
                timestamp = f"[{datetime.now().strftime('%d/%m/%Y, %H:%M:%S')}]"
            
            # If the log file exists, open it and log the message
            if os.path.exists(_logPath):
                message = str(message)
                prefix = str(prefix)
                if prefixBrackets and not prefix == '':
                    prefix = f'[{prefix}] '

                with open(_logPath, 'a') as logFile:
                    logFile.write(f'{timestamp} {prefix}{message}\n')

            # If the log file doesn't exist, create a new one and log the message
            else:
                os.makedirs(Path(_logPath).parent)
                with open(_logPath, 'w') as logFile:
                    logFile.write(f"{timestamp} [ERROR] Log file missing or inaccessible. Creating a new one.\n")

                Logger.Log(message, prefix, prefixBrackets=prefixBrackets, includeTimestamp=includeTimestamp)
                
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
        global _logLevelInt
        if type(level) == str:
            levels = {
                'none': 0,
                'error': 1,
                'warning': 2,
                'success': 3,
                'info': 4,
                'all': 5
            }
            _logLevelInt = levels.get(level.lower(), 1)

        elif type(level) == int or type(level) == Logger.Levels:
            _logLevelInt = level

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
        if os.path.exists(_logPath):
            dateTime = datetime.now().strftime('%d/%m/%Y, %H:%M:%S')
            with open(_logPath, 'w') as logFile:
                logFile.write(f"[{dateTime}] [INFO] Cleared log file contents\n")

        else:
            Logger.Log()

    clear_log = ClearLog

    @staticmethod
    def Set(messageLogging: bool = True, inputLogging: bool = True):
        """
        Enable or disable messsage logging and input logging.

        Parameters:\n
        `messageLogging` - Enable or disable message logging.\n
        `inputLogging` - Enable or disable user input logging.
        """
        global _enableMessageLogging
        global _enableInputLogging
        _enableMessageLogging = messageLogging
        _enableInputLogging = inputLogging

    class Levels:
        """
        Log level constants to use in the `Logger.SetLogLevel()` function.
        """
        NONE = 0
        ERROR = 1
        WARNING = 2
        SUCCESS = 3
        INFO = 4
        ALL = 5

    levels = Levels
    LogLevels = Levels
    log_levels = Levels