from pyconsole import *
import time

# Clear the log file
Logger.ClearLog()
# Log everything into the log file
Logger.SetLogLevel(Logger.Levels.everything)

PrintMessage("This is an error message.", "ERROR")
PrintMessage("This is a warning message.", "WARNING")
PrintMessage("This is a success message.", "SUCCESS")
PrintMessage("This is an info message.", "INFO")
PrintMessage("This is a generic message.")
PrintMessage("This is a message with a custom prefix.", "Custom Prefix")
PrintMessage("This is a message with a custom color.", messageColor=Color.BrightCyan)
PrintMessage("You can combine custom prefixes and colors.", "Example", prefixColor=Color.BrightMagenta)
PrintMessage("You can even override preset message colors.", "ERROR", prefixColor=Color.Blue)
PrintMessage("You can set the colors for the message and prefix separately.", "Example", Color.BrightCyan, Color.Yellow)
PrintMessage("For even more customizability, you can choose whether to color only the prefix,", "INFO", prefixColor=Color.BrightBlue)
PrintMessage("Or the brackets as well.", "INFO", prefixColor=Color.BrightBlue, colorBrackets=True)
PrintMessage("This message has been logged in the log file.", "INFO", forceLog=True)
PrintMessage("\n")

# Create an instance of the progress bar
progressBar = ProgressBar(prefix="Example progress bar:", length=50)
# Update the progress bar every 100 milliseconds, 100 times
for item in range(1, 101):
    time.sleep(0.1)
    progressBar.update(item)

PrintMessage("\n")
UserInput("This is a prompt for input. ")
UserInput("The prompts can be colored. ", Color.BrightYellow)
UserInput("As well as the user's input. ", Color.BrightGreen, Color.Cyan)
UserInput("Press enter to exit the program. ")