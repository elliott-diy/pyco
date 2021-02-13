from py_console import *

# Clear the screen. Fixes a bug in Windows consoles where colors wouldn't show if the console wasnt cleared.
clear()

PrintMessage("This is an error message.", "ERROR")
PrintMessage("This is a warning message.", "WARNING")
PrintMessage("This is a success message.", "SUCCESS")
PrintMessage("This is an info message.", "INFO")
PrintMessage("This is a generic message.", "none")
PrintMessage("This is a message with a custom prefix.", "Custom Prefix")
PrintMessage("This is a message with a custom color.", "none", BrightCyan, True)
PrintMessage("You can combine custom prefixes and colors.", "Example", BrightMagenta)
PrintMessage("You can even override preset message colors.", "ERROR", BrightBlue)
PrintMessage("You can choose whether to color only the prefix,", "INFO", Green)
PrintMessage("Or the whole message.", "INFO", Green, True)
PrintMessage("This message has been logged in the log file.", "INFO", None, False, True)
input("Press ENTER to exit the program.")