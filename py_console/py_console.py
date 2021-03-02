#  _____               _____                      _      
# |  __ \             / ____|                    | |     
# | |__) |   _ ______| |     ___  _ __  ___  ___ | | ___ 
# |  ___/ | | |______| |    / _ \| '_ \/ __|/ _ \| |/ _ \
# | |   | |_| |      | |___| (_) | | | \__ \ (_) | |  __/
# |_|    \__, |       \_____\___/|_| |_|___/\___/|_|\___|
#         __/ |                                          
#        |___/
#
# Made by Duplexes and LemonPi314
# https://github.com/Duplexes/Py-Console

# Imports needed to use this code
import os 
from datetime import datetime
from pathlib import Path

# This must be run when the program starts to clear a color bug on Windows consoles
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

# Old version of the same function but in different form
# Repaced by the lambda above
#def ClearScreen():
#    if os.name == "posix":
#        os.system("clear")
#    else:
#      os.system("cls")

# Get the directory containing the project files
workingDir = os.getcwd()
projectDir = Path(workingDir).parent
logDir = os.path.join(projectDir, "logs", "log.txt")

# Get the type of the operating system being used
osName = os.name

# If the operating system is Windows, clear the console screen to fix the color bug
if osName == "nt":
    clear()

# Massive list of colors to easily use on all console systems
class ConsoleColor:
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

# List of premade UserInput() prefixes
#class ConsoleMessage:
#    Warning = "[\u001b[33;1mWarning\u001b[0m] "
#    Error = "[\u001b[31;1mError\u001b[0m] "
#    Success = "[\u001b[32;1mSuccess\u001b[0m] "
#    Info = "[\u001b[34;1mInfo\u001b[0m] "

# Premade tools and functions 
# Premade message function
def PrintMessage(message, prefix = "none", messageColor = ConsoleColor.White, prefixColor = None, colorBrackets = False, forceLog = False):
    """
    A replacement for "print()" with color and various prefix and logging options.

    Parameters:
    message - The message you want to print
    prefix - The label before the message
    messageColor - The color for the message
    prefixColor - The color for the prefix
    colorBrackets - Choose whether to color the square brackets surrounding the prefix or not
    forceLog - Force the message to be logged regardless of the label
    It is also possible to enter a custom prefix
    """

    log = False
    color = ConsoleColor.White

    if prefix.lower().find("info") != -1:
        color = ConsoleColor.White

    elif prefix.lower().find("success") != -1:
        color = ConsoleColor.BrightGreen

    elif prefix.lower().find("warning") != -1:
        color = ConsoleColor.BrightYellow
        log = True

    elif prefix.lower().find("error") != -1:
        color = ConsoleColor.BrightRed
        log = True

    elif prefix.lower() == "none":
        prefix = ""
        color = ConsoleColor.White

    if prefixColor == None:
        prefixColor = color

    if messageColor == None:
        messageColor = ConsoleColor.White

    if prefix != "":
        if colorBrackets == True:
            prefix = "[" + prefix + "] "
            print(ConsoleColor.Reset + prefixColor + prefix + ConsoleColor.Reset + messageColor + message + ConsoleColor.Reset)

        elif colorBrackets == False:
            print(ConsoleColor.Reset + "[" + prefixColor + prefix + ConsoleColor.Reset + "] " + messageColor + message + ConsoleColor.Reset)        

    elif prefix == "":
        print(ConsoleColor.Reset + messageColor + message + ConsoleColor.Reset)

    if forceLog == True:
        log = True

    if log == True:
        Logger(message, prefix)

# Premade input prompt function
def UserInput(prefix = "", prefixColor = ConsoleColor.White, inputColor = ConsoleColor.White):
    """
    A replacement for "input()" with colors.

    Parameters:
    prefix - The prompt before the program asks for input from the user
    prefixColor - The color for the prompt
    inputColor - The color for the user's input
    """

    input(prefixColor + prefix + ConsoleColor.Reset+ inputColor)

# Function to log entries into a text file
def Logger(message = "", prefix = ""):
    """
    Logging function which writes log entries to a text file.

    Parameters:
    message - The message to be logged
    prefix - The prefix before the message, and after the timestamp
    """

    # Get the date and time
    dateTime = datetime.now()
    dateTime = dateTime.strftime("%d/%m/%Y, %H:%M:%S")
    # If the log file exists, open it and log the message
    if os.path.exists(logDir):
        logfile = open(logDir, "a")
        logfile.write("[" + dateTime + "] " + "[" + prefix + "] " + message + "\n")

    # If the log file doesn't exist, create a new one and log the message
    else:
        logfile = open(logDir, "x")
        logfile.write("[" + dateTime + "] " + "[ERROR] " + "Log file missing or inaccessible. Creating a new one." + "\n")
        ErrorLogger(message, prefix)

# Function to clear the log file
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
ClearLog()

# For testing purposes
#print(ConsoleMessage.Warning + "Somthing could be broken!")
#print(ConsoleMessage.Error + "Error 404!")
#print(ConsoleMessage.Info + "Heres some info!")
#print(ConsoleMessage.Success + "Somthing good happend!")
#input("stop")