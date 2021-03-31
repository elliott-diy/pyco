from pyconsole import *
import time

# Clear the log file
Logger.ClearLog()
# Log everything into the log file
Logger.SetLogLevel(Logger.Levels.ALL)

PrintMessage("This is an error message.", prefix="ERROR")
PrintMessage("This is a warning message.", prefix="WARNING")
PrintMessage("This is a success message.", prefix="SUCCESS")
PrintMessage("This is an info message.", prefix="INFO")
PrintMessage("This is a generic message.")
PrintMessage("This is a message with a custom prefix.", prefix="Custom Prefix")
PrintMessage("This is a message with a custom color.", messageColor=Color.BrightCyan)
PrintMessage("You can combine custom prefixes and colors.", prefix="Example", prefixColor=Color.BrightMagenta)
PrintMessage("You can even override preset message colors.", prefix="ERROR", prefixColor=Color.BrightGreen)
PrintMessage("You can set the colors for the message and prefix separately.", prefix="Example", messageColor=Color.Red, prefixColor=Color.Yellow)
PrintMessage("For even more customizability, you can choose whether to color only the prefix,", prefix="INFO", prefixColor=Color.BrightBlue)
PrintMessage("Or the brackets as well.", prefix="INFO", prefixColor=Color.BrightBlue, colorBrackets=True)
PrintMessage("This message has been logged in the log file.", prefix="INFO", forceLog=True)
PrintMessage("\n")

# Create an instance of the progress bar
progressBar = ProgressBar(prefix="Example progress bar", length=50)
# Update the progress bar every 100 milliseconds, 100 times
for item in range(1, 101):
    progressBar.Update(item)
    time.sleep(0.1)

PrintMessage("\n")
UserInput("This is a prompt for input. ")
UserInput("The prompts can be colored. ", Color.BrightYellow)
UserInput("As well as the user's input. ", Color.BrightGreen, Color.Cyan)
UserInput("Press enter to exit the program. ")