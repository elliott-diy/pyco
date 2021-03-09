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

# Imports needed to use this code
import os 
from datetime import datetime
from pathlib import Path

# This must be run when the program starts to clear a color bug on Windows consoles
ClearScreen = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Old version of the same function but in different form
# Repaced by the lambda above
#def ClearScreen():
#    if os.name == "posix":
#        os.system("clear")
#    else:
#      os.system("cls")

# Get the directory containing the project files
workingDir = os.getcwd()
projectDir = Path(workingDir)
logDir = os.path.join(projectDir, "logs", "log.txt")

# Get the type of the operating system being used
osName = os.name

# If the operating system is Windows, clear the console screen to fix the color bug
if osName == "nt":
    ClearScreen()

# Variables to enable or disable logging and log clearing
enableMessageLogging = True
enableInputLogging = True
clearLogOnStart = True

# Set default log level
logLevelInt = 3

# Massive list of colors to easily use on all console systems
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

#class LogLevel:
#    none = 0
#    error = 1
#    warning = 2
#    success = 3
#    info = 4
#    All = 5

# List of premade UserInput() prefixes
#class ConsoleMessage:
#    Warning = "\u001b[0m[\u001b[33;1mWarning\u001b[0m] "
#    Error = "\u001b[0m[\u001b[31;1mError\u001b[0m] "
#    Success = "\u001b[0m[\u001b[32;1mSuccess\u001b[0m] "
#    Info = "\u001b[0m[\u001b[34;1mInfo\u001b[0m] "

# Premade tools and functions 
def PrintMessage(message, prefix = "none", messageColor = Color.White, prefixColor = None, colorBrackets = False, forceLog = False):
    """
    A replacement for "print()" with color and various prefix and logging options. 

    Parameters: 
    message - The message you want to print. 
    prefix - The label before the message. 
    messageColor - The color for the message. 
    prefixColor - The color for the prefix. 
    colorBrackets - Choose whether to color the square brackets surrounding the prefix or not. 
    forceLog - Force the message to be logged regardless of the label. 
    It is also possible to enter a custom prefix. 
    """

    log = False
    color = Color.White
    
    if prefix.lower().find("error") != -1:
        color = Color.BrightRed

        if logLevelInt >= 1:
            log = True

    elif prefix.lower().find("warning") != -1:
        color = Color.BrightYellow

        if logLevelInt >= 2:
            log = True

    elif prefix.lower().find("success") != -1:
        color = Color.BrightGreen

        if logLevelInt >= 3:
            log = True

    elif prefix.lower().find("info") != -1:
        color = Color.White

        if logLevelInt >= 4:
            log = True

    elif prefix.lower() == "none":
        prefix = ""
        color = Color.White

        if logLevelInt == 5:
            log = True

    if prefixColor == None:
        prefixColor = color
        
    if messageColor == None:
        messageColor = Color.White

    if forceLog == True:
        log = True

    if log == True:
        Logger(message, prefix)

    if prefix != "":
        if colorBrackets == True:
            prefix = "[" + prefix + "] "
            print(Color.Reset + prefixColor + prefix + Color.Reset + messageColor + message + Color.Reset)

        elif colorBrackets == False:
            print(Color.Reset + "[" + prefixColor + prefix + Color.Reset + "] " + messageColor + message + Color.Reset)        

    elif prefix == "":
        print(Color.Reset + messageColor + message + Color.Reset)

def UserInput(prefix = "", prefixColor = Color.White, inputColor = Color.White):
    """
    A replacement for "input()" with colors. 

    Parameters: 
    prefix - The prompt before the program asks for input from the user. 
    prefixColor - The color for the prompt. 
    inputColor - The color for the user's input. 
    """

    userInput = input(prefixColor + prefix + Color.Reset+ inputColor)

    if enableMessageLogging == True:
        Logger(userInput, prefix, False)

    return userInput

def ProgressBar(iteration, total, prefix = "", suffix = "", length = 100, fill = "█", decimals = 1, printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar. 

    Parameters: 
    iteration - Required. Current iteration (Int). 
    total - Required. Total iterations (Int). 
    prefix - Optional. Prefix string (Str). 
    suffix - Optional. Suffix string (Str). 
    length - Optional. Character length of bar (Int). 
    fill - Optional. Bar fill character (Str). 
    decimals - Optional. Positive number of decimals in percent complete (Int). 
    printEnd - Optional. End character (e.g. "\r", "\r\n") (Str). 
    """

    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)

    # Print new line on complete
    if iteration == total: 
        print()

def Logger(message = "", prefix = "", prefixBrackets = True):
    """
    Logging function which writes log entries to a text file. 

    Parameters: 
    message - The message to be logged. 
    prefix - The prefix before the message, and after the timestamp. 
    """

    if enableMessageLogging == True:
        # Get the date and time
        dateTime = datetime.now()
        dateTime = dateTime.strftime("%d/%m/%Y, %H:%M:%S")

        if os.path.exists(Path(logDir).parent):
            # If the log file exists, open it and log the message
            if os.path.exists(logDir):
                logfile = open(logDir, "a")

                if prefix == "" or prefixBrackets == False:
                    logfile.write("[" + dateTime + "] " + prefix + message + "\n")
                
                else:
                    logfile.write("[" + dateTime + "] " + "[" + prefix + "] " + message + "\n")

        # If the log file doesn't exist, create a new one and log the message
        else:
            os.makedirs(Path(logDir).parent)
            logfile = open(logDir, "x")
            logfile.write("[" + dateTime + "] " + "[ERROR] " + "Log file missing or inaccessible. Creating a new one." + "\n")
            Logger(message, prefix)
        
        logfile.close()

def SetLogLevel(level):
    """
    Set the log level. 
    
    Parameters: 
    level - String. 
    
    "none" - Don't log any messages. 
    "error" - Log errors. 
    "warning" - Log warnings and errors. 
    "success" - Log successes, warnings, and errors. 
    "info" - Log info, successes, warnings, and errors. 
    "all" - Log everything. 
    """

    if type(level) == str:
        levels = {
            "none": 0,
            "error": 1,
            "warning": 2,
            "success": 3,
            "info": 4,
            "all": 5
        }

        logLevelInt = levels.get(level, 1)

    elif type(level) == int:
        logLevelInt = level

def ClearLog():
    """
    Clear the log file to save disk space. 
    The file will still exist with one entry, it will not get deleted. 
    """

    if os.path.exists(logDir):
        dateTime = datetime.now()
        dateTime = dateTime.strftime("%d/%m/%Y, %H:%M:%S")
        logfile = open(logDir, "w")
        logfile.write("[" + dateTime + "] " + "[INFO] " + "Cleared log file contents" + "\n")
        logfile.close()

    else:
        Logger()
    
# Clear the error log file on startup
if clearLogOnStart == True:
    ClearLog()