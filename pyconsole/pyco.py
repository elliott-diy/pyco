#                                        _      
#                                       | |     
#  _ __  _   _  ___ ___  _ __  ___  ___ | | ___ 
# | '_ \| | | |/ __/ _ \| '_ \/ __|/ _ \| |/ _ \
# | |_) | |_| | (_| (_) | | | \__ \ (_) | |  __/
# | .__/ \__, |\___\___/|_| |_|___/\___/|_|\___|
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

# Hack to get Windows consoles to show colors
if osName == 'nt':
    import subprocess
    subprocess.call('', shell=True)

def PrintMessage(message: str = '', prefix: str = 'none', messageColor: Color = Color.AUTO, prefixColor: Color = None, colorBrackets: bool = False, forceLog: bool = None, sep: str = ' ', end: str = '\n', flush: bool = False):
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
    if prefix.lower().find('error') != -1:
        autoPrefixColor = Color.ERROR
        if Logger._logLevelInt >= 1:
            log = True

    elif prefix.lower().find('warning') != -1:
        autoPrefixColor = Color.WARNING
        if Logger._logLevelInt >= 2:
            log = True

    elif prefix.lower().find('success') != -1:
        autoPrefixColor = Color.SUCCESS
        if Logger._logLevelInt >= 3:
            log = True

    elif prefix.lower().find('info') != -1:
        autoPrefixColor = Color.INFO
        if Logger._logLevelInt >= 4:
            log = True

    elif prefix.lower() == 'none' or prefix is None:
        prefix = ''
        autoPrefixColor = Color.DEFAULT_PREFIX_COLOR
        if Logger._logLevelInt == 5:
            log = True

    if prefixColor is None or prefixColor == Color.AUTO:
        prefixColor = autoPrefixColor
        
    if messageColor is None or prefixColor == Color.AUTO:
        messageColor = Color.DEFAULT_MESSAGE_COLOR

    if forceLog is not None:
        log = forceLog

    if log and Logger.enableMessageLogging:
        Logger.Log(message, prefix)

    if prefix != '':
        if colorBrackets is True:
            print(f'{Color.RESET}{prefixColor}[{prefix}] {Color.RESET}{messageColor}{message}{Color.RESET}', sep=sep, end=end, flush=flush)

        elif colorBrackets is False:
            print(f'{Color.RESET}[{prefixColor}{prefix}{Color.RESET}] {messageColor}{message}{Color.RESET}', sep=sep, end=end, flush=flush)

    elif prefix == '':
        print(Color.RESET + messageColor + message + Color.RESET)

Print = PrintMessage
print_message = PrintMessage
PrintMsg = PrintMessage
print_msg = PrintMessage

def UserInput(prefix: str = '', prefixColor: Color = Color.Foreground.WHITE, inputColor: Color = Color.Foreground.WHITE):
    """
    A replacement for `input()` with colors.

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

        if force is False and self.iteration < self.total and (now - self.lastUpdateTime) < (self.updateIntervalms / 1000):
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