from py_console import *

# Clear the screen. Fixes a bug in Windows consoles where colors wouldn't show if the console wasnt cleared.
clear()

PrintMessage("This is an error message.", "ERROR")
PrintMessage("This is a warning message.", "WARNING")
PrintMessage("This is a success message.", "SUCCESS")
PrintMessage("This is an info message.", "INFO")
PrintMessage("This is a generic message.", "none")
PrintMessage("This is a message with a custom prefix.", "Custom Prefix")
PrintMessage("This is a message with a custom color.", "none", ConsoleColor.BrightCyan, True)
PrintMessage("You can combine custom prefixes and colors.", "Example", ConsoleColor.BrightMagenta)
PrintMessage("You can even override preset message colors.", "ERROR", ConsoleColor.BrightBlue)
PrintMessage("You can choose whether to color only the prefix,", "INFO", ConsoleColor.Green)
PrintMessage("Or the whole message.", "INFO", ConsoleColor.Green, True)
PrintMessage("This message has been logged in the log file.", "INFO", None, False, True)
PrintMessage("\n")
UserInput("This is a prompt for input. ")
UserInput("The prompts can be colored. ", ConsoleColor.BrightYellow)
UserInput("As well as the user's input. ", ConsoleColor.BrightGreen, ConsoleColor.Cyan)
UserInput("Press ENTER to exit the program. ")