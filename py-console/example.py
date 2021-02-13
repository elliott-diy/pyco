from py_console import *

clear()
def ClearScreen():
    if os.name == "posix":
        os.system("clear")
    else:
      os.system("cls")

#ClearScreen()
PrintMessage("This is an error message.", "error")
PrintMessage("This is a warning message.", "warning")
PrintMessage("This is an info message.", "info")
PrintMessage("This is a success message.", "success")
PrintMessage("This is a generic message.", "none")
PrintMessage("This is a message with a custom prefix.", "Custom Prefix")
PrintMessage("This is a message with a custom color.", "none", BrightCyan)
PrintMessage("You can combine custom prefixes and colors.", "Example", BrightMagenta)
PrintMessage("You can even override preset message colors.", "error", "BrightBlue")
PrintMessage("This message has been logged in the log file", "info", None, True)
input("Press ENTER to exit the program.")