from pyconsole import *
import time

SetLogLevel("all")

PrintMessage("This is an error message.", "ERROR")
PrintMessage("This is a warning message.", "WARNING")
PrintMessage("This is a success message.", "SUCCESS")
PrintMessage("This is an info message.", "INFO")
PrintMessage("This is a generic message.")
PrintMessage("This is a message with a custom prefix.", "Custom Prefix")
PrintMessage("This is a message with a custom color.", "none", Color.BrightCyan)
PrintMessage("You can combine custom prefixes and colors.", "Example", Color.White, Color.BrightMagenta)
PrintMessage("You can even override preset message colors.", "ERROR", Color.White, Color.Blue)
PrintMessage("You can set the colors for the message and prefix separately.", "Example", Color.BrightCyan, Color.Yellow)
PrintMessage("For even more customizability, you can choose whether to color only the prefix,", "INFO", Color.White, Color.BrightBlue)
PrintMessage("Or the brackets as well.", "INFO", Color.White, Color.BrightBlue, True)
PrintMessage("This message has been logged in the log file.", "INFO", Color.White, Color.White, False, True)
PrintMessage("\n")

ProgressBar(0, 50, "Example progress bar:", "Complete", 50)
for item in range(0, 50):
    time.sleep(0.1)
    ProgressBar(item + 1, 50, "Example progress bar:", "Complete", 50)

PrintMessage("\n")
UserInput("This is a prompt for input. ")
UserInput("The prompts can be colored. ", Color.BrightYellow)
UserInput("As well as the user's input. ", Color.BrightGreen, Color.Cyan)
UserInput("Press ENTER to exit the program. ")