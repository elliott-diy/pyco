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

# (Formerly)
#  _____       _   _              _______          _     
# |  __ \     | | | |            |__   __|        | |    
# | |__) |   _| |_| |__   ___  _ __ | | ___   ___ | |___ 
# |  ___/ | | | __| '_ \ / _ \| '_ \| |/ _ \ / _ \| / __|
# | |   | |_| | |_| | | | (_) | | | | | (_) | (_) | \__ \
# |_|    \__, |\__|_| |_|\___/|_| |_|_|\___/ \___/|_|___/
#         __/ |                                          
#        |___/                                           
#
# Made by Duplexes

# Imports needed to use this code
import os 
from datetime import datetime
from pathlib import Path

# Massive list of colors to easily use on all console systems
class ConsoleColor:
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
class ConsoleMessage:
    Warning = "[\u001b[33;1mWarning\u001b[0m] "
    Error = "[\u001b[31;1mError\u001b[0m] "
    Success = "[\u001b[32;1mSuccess\u001b[0m] "
    Info = "[\u001b[34;1mInfo\u001b[0m] "

    

# Premade message function
# Parameters:
# message - The message you want to print
# prefix - The label before the message
# forceColor - Specify a color to be used instead of the default
# colorMessage - Choose whether to color only the prefix or the whole message
# forceLog - Force the message to be logged regardless of the label
# It is also possible to enter a custom prefix
def PrintMessage(message, prefix = "none", forceColor = None, colorMessage = False, forceLog = False):
    log = False
    color = ConsoleColor.White

    if prefix.lower() == "info":
        color = ConsoleColor.White

    elif prefix.lower() == "success":
        color = ConsoleColor.BrightGreen

    elif prefix.lower() == "warning":
        color = ConsoleColor.BrightYellow
        log = True

    elif prefix.lower() == "error":
        color = ConsoleColor.BrightRed
        log = True

    elif prefix.lower() == "none":
        prefix = ""
        color = ConsoleColor.White

    if prefix != "":
        prefix = "[" + prefix + "] "

    if forceLog == True:
        log = True

    if forceColor != None:
        color = forceColor

    if colorMessage == False:
        print(color + prefix + ConsoleColor.Reset + message)

    if colorMessage == True:
        print(color + prefix + message + ConsoleColor.Reset)

    if log == True:
        Logger(message, prefix)

# Premade input prompt function
# Parameters:
# prefix - The prompt before the program asks for input from the user
# prefixColor - The color for the prompt
# inputColor - The color for the user's input
def UserInput(prefix = "", prefixColor = ConsoleColor.White, inputColor = ConsoleColor.White):
    input(prefixColor + prefix + ConsoleColor.Reset+ inputColor)

# Premade tools and functions/lambdas 
# This must be run when the program starts to clear a color bug on Windows consoles.
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

def Logger(message = "", prefix = ""):
    # Get the date and time
    dateTime = datetime.now()
    dateTime = dateTime.strftime("%d/%m/%Y, %H:%M:%S")
    # If the log file exists, open it and log the message
    if os.path.exists(logDir):
        logfile = open(logDir, "a")
        logfile.write("[" + dateTime + "] " + prefix + message + "\n")

    # If the log file doesn't exist, create a new one and log the message
    else: 
        logfile = open(logDir, "x")
        logfile.write("[" + dateTime + "] " + "[ERROR] " + "Log file missing or inaccessible. Creating a new one." + "\n")
        ErrorLogger(message, prefix)

# Function to clear the log file. 
def ClearLog():
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

clear()
print(ConsoleMessage.Warning + "Somthing could be broken!")
print(ConsoleMessage.Error + "Error 404!")
print(ConsoleMessage.Info + "Heres some info!")
print(ConsoleMessage.Success + "Somthing good happend!")
input("stop")