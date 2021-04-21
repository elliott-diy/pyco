#  _ __  _   _  ___ ___  
# | '_ \| | | |/ __/ _ \ 
# | |_) | |_| | (_| (_) |
# | .__/ \__, |\___\___/ 
# | |     __/ |          
# |_|    |___/           

import os, time, atexit
from .ansi import *
from .logger import *

atexit.register(Terminal.ResetAll)

osName = os.name

ClearScreenCommand = lambda: os.system('cls' if osName == 'nt' else 'clear')

clear_screen_command = ClearScreenCommand
clearscreen = ClearScreenCommand
clear_screen = ClearScreenCommand
clear = ClearScreenCommand
cls = ClearScreenCommand

def ClearScreenFunction():
    if osName == 'nt':
        os.system('cls')

    else:
        os.system('clear')

ClearScreenFunc = ClearScreenFunction
clear_screen_function = ClearScreenFunction
clearscreen_func = ClearScreenFunction
clear_screen_func = ClearScreenFunction
clear_func = ClearScreenFunction
cls_func = ClearScreenFunction

if osName == 'nt':
    from .utils import WindowsConsole
    WindowsConsole().enable_vt_mode()

def PrintMessage(message: str = '', prefix: str = None, messageColor: Color = Color.AUTO, prefixColor: Color = Color.AUTO, colorBrackets: bool = False, forceLog: bool = None, sep: str = ' ', end: str = '\n', flush: bool = False):
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
    autoPrefixColor = Color.DEFAULT_PREFIX_COLOR
    
    if prefix is None:
        prefix = ''
        autoPrefixColor = Color.DEFAULT_PREFIX_COLOR
    
    elif prefix.lower().find('error') != -1:
        autoPrefixColor = Color.ERROR
        if Logger.logLevel >= Logger.Levels.ERROR:
            log = True

    elif prefix.lower().find('warning') != -1:
        autoPrefixColor = Color.WARNING
        if Logger.logLevel >= Logger.Levels.WARNING:
            log = True

    elif prefix.lower().find('success') != -1:
        autoPrefixColor = Color.SUCCESS
        if Logger.logLevel >= Logger.Levels.SUCCESS:
            log = True

    elif prefix.lower().find('info') != -1:
        autoPrefixColor = Color.INFO
        if Logger.logLevel >= Logger.Levels.INFO:
            log = True

    if Logger.logLevel == Logger.Levels.ALL:
            log = True

    if prefixColor is None or prefixColor == Color.AUTO:
        prefixColor = autoPrefixColor
        
    if messageColor is None or messageColor == Color.AUTO:
        messageColor = Color.DEFAULT_MESSAGE_COLOR

    if forceLog is not None:
        log = forceLog

    if log and Logger.enableMessageLogging:
        Logger.Log(message, prefix)

    if prefix != '':
        if colorBrackets is True:
            print(f'{Color.RESET}{prefixColor}[{prefix}]{Color.RESET} {messageColor}{message}{Color.RESET}', sep=sep, end=end, flush=flush)

        elif colorBrackets is False:
            print(f'{Color.RESET}[{prefixColor}{prefix}{Color.RESET}] {messageColor}{message}{Color.RESET}', sep=sep, end=end, flush=flush)

    elif prefix == '':
        print(f'{Color.RESET}{messageColor}{message}{Color.RESET}')

Print = PrintMessage
print_message = PrintMessage
PrintMsg = PrintMessage
print_msg = PrintMessage

def UserInput(prefix: str = '', prefixColor: Color = Color.DEFAULT_PREFIX_COLOR, inputColor: Color = Color.DEFAULT_MESSAGE_COLOR):
    """
    A replacement for `input()` with colors and logging.

    Parameters:\n
        `prefix` - The prompt before user's input.\n
        `prefixColor` - The color for the prompt.\n
        `inputColor` - The color for the user's input.
    """
    prefix = str(prefix)
    userInput = input(Color.RESET + prefixColor + prefix + Color.RESET + inputColor)
    if Logger.enableInputLogging is True:
        Logger.Log(userInput, prefix, False)

    return userInput

Input = UserInput
userinput = UserInput
user_input = UserInput

class ProgressBar:
    def __init__(self, iteration: int = 0, total: int = 100, prefix: str = '', suffix: str = '', length: int = 100, fill: str = '█', emptyFill: str = '-', decimals: int = 1, end: str = '\r', updateIntervalms: float = 100):
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
            `emptyFill` - Character to fill in empty part of the bar.\n
            `decimals` - Positive number of decimals in percent complete.\n
            `end` - End character (e.g. `'\\r'`, `'\\r\\n'`).
        """
        self.iteration = iteration
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.emptyFill = emptyFill
        self.decimals = decimals
        self.end = end
        self.updateIntervalms = updateIntervalms
        self.lastUpdateTime: time = 0
    
    def Update(self, iteration = None, force = False):
        now = time.time()
        if iteration != None:
            self.iteration = iteration

        if self.updateIntervalms == 0:
            self.updateIntervalms = 1

        if force is False and self.iteration < self.total and (now - self.lastUpdateTime) < (self.updateIntervalms / 1000):
            return
            
        self.lastUpdateTime = now
        ProgressBar._PrintProgressBar(iteration=self.iteration, total=self.total, prefix=self.prefix, suffix=self.suffix, length=self.length, fill=self.fill, emptyFill=self.emptyFill, decimals=self.decimals, end=self.end)
        if self.iteration == self.total:
            print()

    update = Update

    @staticmethod
    def _PrintProgressBar(iteration: int, total: int, prefix: str = '', suffix: str = '', length: int = 100, fill: str = '█', emptyFill: str = '-', decimals: int = 1, end: str = '\r'):
        percent = f'{round(100 * (iteration / total), int(decimals))}'
        filledLength = int(length * iteration // total)
        bar = (fill * filledLength) + (emptyFill * (length - filledLength))
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=end)