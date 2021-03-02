from Py_Console import *

# Clear the screen. Fixes a bug in Windows consoles where colors wouldn't show if the console wasn't cleared.
clear()

PrintMessage("This is an error message.", "ERROR")
PrintMessage("This is a warning message.", "WARNING")
PrintMessage("This is a success message.", "SUCCESS")
PrintMessage("This is an info message.", "INFO")
PrintMessage("This is a generic message.")
PrintMessage("This is a message with a custom prefix.", "Custom Prefix")
PrintMessage("This is a message with a custom color.", "none", ConsoleColor.BrightCyan)
PrintMessage("You can combine custom prefixes and colors.", "Example", ConsoleColor.White, ConsoleColor.BrightMagenta)
PrintMessage("You can even override preset message colors.", "ERROR", ConsoleColor.White, ConsoleColor.Blue)
PrintMessage("You can set the colors for the message and prefix separately.", "Example", ConsoleColor.BrightCyan, ConsoleColor.Yellow)
PrintMessage("For even more customizability, you can choose whether to color only the prefix,", "INFO", ConsoleColor.White, ConsoleColor.BrightBlue)
PrintMessage("Or the brackets as well.", "INFO", ConsoleColor.White, ConsoleColor.BrightBlue, True)
PrintMessage("This message has been logged in the log file.", "INFO", ConsoleColor.White, ConsoleColor.White, False, True)
PrintMessage("\n")
UserInput("This is a prompt for input. ")
UserInput("The prompts can be colored. ", ConsoleColor.BrightYellow)
UserInput("As well as the user's input. ", ConsoleColor.BrightGreen, ConsoleColor.Cyan)
UserInput("Press ENTER to exit the program. ")