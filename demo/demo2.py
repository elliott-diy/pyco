from pyco import *

# Clear the log file
Logger.ClearLog()
# Set the logger to log all messages
Logger.SetLogLevel(Logger.Levels.ALL)
# Log a message
Logger.Log("This is a log message", "Log prefix")
# Disable logging
Logger.enableMessageLogging = False
# Disable input logging
Logger.enableInputLogging = False
# Enable message and input logging
Logger.enableMessageLogging = Logger.enableInputLogging = True

PrintMessage("Generic message")
PrintMessage("Error message", "Error")
PrintMessage("Warning message", "Warning")
PrintMessage("Success message", "Success")
PrintMessage("Info message", "Info")
PrintMessage("Message in pink", "none", messageColor=Color.Fore.BRIGHT_MAGENTA)
PrintMessage("Message in blue", "Green prefix", messageColor=Color.Fore.BLUE, prefixColor=Color.Fore.GREEN)
PrintMessage("Message in cyan The brackets around the prefix are also colored", "Custom Prefix", messageColor=Color.Fore.BRIGHT_YELLOW, prefixColor=Color.Fore.RED, colorBrackets=True)
PrintMessage("This message has been logged in the log file", "Info", forceLog=True)
PrintMessage("Bright white text on green background", messageColor=Color.Fore.BRIGHT_WHITE + Color.Back.GREEN)

UserInput("Prompt. ")
UserInput("Prompt in green. ", prefixColor=Color.Fore.GREEN)
UserInput("Prompt in bright red, user input in blue. ", prefixColor=Color.Fore.BRIGHT_RED, inputColor=Color.Fore.BLUE)

progressBar = ProgressBar()
for i in range(1, 101):
    progressBar.Update(i)

print(Color.Fore.RED + "I'm red!")
print(Color.Fore.BRIGHT_GREEN + "I'm bright green!")