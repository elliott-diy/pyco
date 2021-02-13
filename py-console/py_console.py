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
Black = "\u001b[30m"    
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta =  "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"                # Used in premade messages. Must be included to function correctly.
Reset = "\u001b[0m"                 # Used in premade messages. Must be included to function correctly.
BrightBlack = "\u001b[30;1m"
BrightRed = "\u001b[31;1m"          # Used in premade messages. Must be included to function correctly. 
BrightGreen = "\u001b[32;1m"        # Used in premade messages. Must be included to function correctly.
BrightYellow = "\u001b[33;1m"       # Used in premade messages. Must be included to function correctly.
BrightBlue = "\u001b[34;1m"
BrightMagenta = "\u001b[35;1m"
BrightCyan = "\u001b[36;1m"         # Used in premade messages. Must be included to function correctly.
BrightWhite = "\u001b[37;1m"

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
    color = White

    if prefix.lower() == "info":
        color = White

    elif prefix.lower() == "success":
        color = BrightGreen

    elif prefix.lower() == "warning":
        color = BrightYellow
        log = True

    elif prefix.lower() == "error":
        color = BrightRed
        log = True

    elif prefix.lower() == "none":
        prefix = ""
        color = White
    if prefix != "":
        prefix = "[" + prefix + "] "

    if forceLog == True:
        log = True

    if forceColor != None:
        color = forceColor

    if colorMessage == False:
        print(color + prefix + Reset + message)

    if colorMessage == True:
        print(color + prefix + message + Reset)

    if log == True:
        Logger(message, prefix)

# Placeholder funtion for inputs with color
def UserInput(prefix, color):
    print(prefix)

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
workingDir = Path(__file__).parent
projectDir = Path(__file__).parent.parent
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