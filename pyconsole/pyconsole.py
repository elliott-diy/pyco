#                                        _      
#                                       | |     
#  _ __  _   _  ___ ___  _ __  ___  ___ | | ___ 
# | '_ \| | | |/ __/ _ \| '_ \/ __|/ _ \| |/ _ \
# | |_) | |_| | (_| (_) | | | \__ \ (_) | |  __/
# | .__/ \__, |\___\___/|_| |_|___/\___/|_|\___|
# | |     __/ |                                 
# |_|    |___/ 
#
# Made by Duplexes and LemonPi314
# https://github.com/Duplexes/pyconsole

import os, time
from datetime import datetime
from pathlib import Path

# This must be run when the program starts to clear a color bug on Windows consoles
ClearScreen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def ClearScreenFunction():
    if os.name == "nt":
        os.system("cls")

    else:
        os.system("clear")

# Get the name of the current operating system
osName = os.name

# If the operating system is Windows, clear the console screen to fix the color bug
if osName == "nt":
    ClearScreen()

# Get the directory containing the project files
workingDir = os.getcwd()
projectDir = Path(workingDir)

# Set the default log file directory
_logDir = os.path.join(projectDir, "logs", "log.txt")

# Variables to enable or disable message logging and input logging
_enableMessageLogging = True
_enableInputLogging = True

# Set default log level
_logLevelInt = 3

class Color:
    """
    A list of colors as console escape codes.
    """
    Reset = "\u001b[0m"
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta =  "\u001b[35m"
    Cyan = "\u001b[36m"
    White = "\u001b[37m"
    BrightBlack = "\u001b[30;1m"
    BrightRed = "\u001b[31;1m"
    BrightGreen = "\u001b[32;1m"
    BrightYellow = "\u001b[33;1m"
    BrightBlue = "\u001b[34;1m"
    BrightMagenta = "\u001b[35;1m"
    BrightCyan = "\u001b[36;1m"
    BrightWhite = "\u001b[37;1m"

# Premade tools and functions 
def PrintMessage(message = "", prefix = "none", messageColor: Color = Color.White, prefixColor: Color = None, colorBrackets: bool = False, forceLog: bool = None):
    """
    A replacement for `print()` with color and various prefix and logging options. 

    Parameters: 
    `message` - The message you want to print. 
    `prefix` - The label before the message. 
    `messageColor` - The color for the message. 
    `prefixColor` - The color for the prefix. 
    `colorBrackets` - Choose whether to color the square brackets surrounding the prefix or not. 
    `forceLog` - Force the message to be logged regardless of the label. 
    It is also possible to enter a custom prefix. 
    """
    log = False
    color = Color.White
    if prefix.lower().find("error") != -1:
        color = Color.BrightRed
        if _logLevelInt >= 1:
            log = True

    elif prefix.lower().find("warning") != -1:
        color = Color.BrightYellow
        if _logLevelInt >= 2:
            log = True

    elif prefix.lower().find("success") != -1:
        color = Color.BrightGreen
        if _logLevelInt >= 3:
            log = True

    elif prefix.lower().find("info") != -1:
        color = Color.White
        if _logLevelInt >= 4:
            log = True

    elif prefix.lower() == "none":
        prefix = ""
        color = Color.White
        if _logLevelInt == 5:
            log = True

    if prefixColor == None:
        prefixColor = color
        
    if messageColor == None:
        messageColor = Color.White

    if forceLog != None:
        log = forceLog

    if log == True:
        Logger.Log(message, prefix)

    if prefix != "":
        if colorBrackets == True:
            prefix = "[" + prefix + "] "
            print(Color.Reset + prefixColor + prefix + Color.Reset + messageColor + message + Color.Reset)

        elif colorBrackets == False:
            print(Color.Reset + "[" + prefixColor + prefix + Color.Reset + "] " + messageColor + message + Color.Reset)        

    elif prefix == "":
        print(Color.Reset + messageColor + message + Color.Reset)

def UserInput(prefix = "", prefixColor: Color = Color.White, inputColor: Color = Color.White):
    """
    A replacement for `input()` with colors. 

    Parameters: 
    `prefix` - The prompt before the program asks for input from the user. 
    `prefixColor` - The color for the prompt. 
    `inputColor` - The color for the user's input. 
    """
    userInput = input(prefixColor + prefix + Color.Reset+ inputColor)
    if _enableInputLogging == True:
        Logger.Log(userInput, prefix, False)

    return userInput

class ProgressBar:
    """
    Create an instance of this class to create a progress bar in the console using `p = ProgressBar()`. 
    To update the progress bar call `p.update(counter)` in a loop where `counter` is increased every iteration. 

    Parameters: 
    `iteration` - Current iteration. 
    `total` - Total iterations. 
    `prefix` - Prefix string. 
    `suffix` - Suffix string. 
    `length` - Character length of bar. 
    `fill` - Bar fill character. 
    `decimals` - Positive number of decimals in percent complete. 
    `printEnd` - End character (e.g. `"\r"`, `"\r\n"`). 
    """
    def __init__(self, iteration: int = 0, total: int = 100, updateIntervalms: float = 100, prefix = "", suffix = "", length: int = 100, fill = "█", decimals: int = 1, printEnd = "\r"):
        self.iteration = iteration
        self.total = total
        self.updateIntervalms = updateIntervalms
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.decimals = decimals
        self.printEnd = printEnd
        self.lastUpdateTime: time = 0
    
    def update(self, iteration = None, force = False):
        now = time.time()
        if iteration != None:
            self.iteration = iteration

        if self.updateIntervalms == 0:
            self.updateIntervalms = 1

        if force == False and self.iteration < self.total and (now - self.lastUpdateTime) < (self.updateIntervalms / 1000):
            return
            
        self.lastUpdateTime = now
        ProgressBar.PrintProgressBar(self.iteration, self.total, self.prefix, self.suffix, self.length, self.fill, self.decimals, self.printEnd)
        if self.iteration == self.total:
            print()

    @staticmethod
    def PrintProgressBar(iteration: int, total: int, prefix = "", suffix = "", length: int = 100, fill = "█", decimals: int = 1, printEnd = "\r"):
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

class Logger:
    @staticmethod
    def Log(message = "", prefix = "", prefixBrackets: bool = True):
        """
        Logging function which writes log entries to a text file. 

        Parameters: 
        `message` - The message to be logged. 
        `prefix` - The prefix before the message, and after the timestamp. 
        """
        if _enableMessageLogging == True:
            # Get the date and time
            dateTime = datetime.now()
            dateTime = dateTime.strftime("%d/%m/%Y, %H:%M:%S")
            if os.path.exists(Path(_logDir).parent):
                # If the log file exists, open it and log the message
                if os.path.exists(_logDir):
                    logFile = open(_logDir, "a")
                    if prefix == "" or prefixBrackets == False:
                        logFile.write("[" + dateTime + "] " + prefix + message + "\n")
                    
                    else:
                        logFile.write("[" + dateTime + "] " + "[" + prefix + "] " + message + "\n")

            # If the log file doesn't exist, create a new one and log the message
            else:
                os.makedirs(Path(_logDir).parent)
                logFile = open(_logDir, "x")
                logFile.write("[" + dateTime + "] " + "[ERROR] " + "Log file missing or inaccessible. Creating a new one." + "\n")
                Logger.Log(message, prefix)
            
            logFile.close()

    @staticmethod
    def SetLogLevel(level):
        """
        Set the log level. 
        
        Parameters: 
        `level` - String. 
        
        `"none"` - Don't log any messages. 
        `"error"` - Log errors. 
        `"warning"` - Log warnings and errors. 
        `"success"` - Log successes, warnings, and errors. 
        `"info"` - Log info, successes, warnings, and errors. 
        `"everything"` - Log everything. 
        """
        global _logLevelInt
        if type(level) == str:
            levels = {
                "none": 0,
                "error": 1,
                "warning": 2,
                "success": 3,
                "info": 4,
                "everything": 5
            }
            _logLevelInt = levels.get(level, 1)

        elif type(level) == int or type(level) == Logger.Levels:
            _logLevelInt = level

    @staticmethod
    def ClearLog():
        """
        Clear the log file to save disk space. 
        The file will still exist with one entry, it will not get deleted. 
        """
        if os.path.exists(_logDir):
            dateTime = datetime.now()
            dateTime = dateTime.strftime("%d/%m/%Y, %H:%M:%S")
            logFile = open(_logDir, "w")
            logFile.write("[" + dateTime + "] " + "[INFO] " + "Cleared log file contents" + "\n")
            logFile.close()

        else:
            Logger.Log()

    @staticmethod
    def Set(messageLogging: bool = True, inputLogging: bool = True):
        """
        Enable or disable messsage logging and input logging. 

        Parameters: 
        `messageLogging` - Enable or disable message logging.
        `inputLogging` - Enable or disable user input logging.
        """
        global _enableMessageLogging
        global _enableInputLogging
        _enableMessageLogging = messageLogging
        _enableInputLogging = inputLogging

    class Levels:
        """
        A list of log levels to use in the `Logger.SetLogLevel()` function.
        """
        none = 0
        error = 1
        warning = 2
        success = 3
        info = 4
        everything = 5