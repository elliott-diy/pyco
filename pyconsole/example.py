from pyconsole import pyconsole

pyconsole.logLevel = "all"

pyconsole.PrintMessage("This is an error message.", "ERROR")
pyconsole.PrintMessage("This is a warning message.", "WARNING")
pyconsole.PrintMessage("This is a success message.", "SUCCESS")
pyconsole.PrintMessage("This is an info message.", "INFO")
pyconsole.PrintMessage("This is a generic message.")
pyconsole.PrintMessage("This is a message with a custom prefix.", "Custom Prefix")
pyconsole.PrintMessage("This is a message with a custom color.", "none", pyconsole.Color.BrightCyan)
pyconsole.PrintMessage("You can combine custom prefixes and colors.", "Example", pyconsole.Color.White, pyconsole.Color.BrightMagenta)
pyconsole.PrintMessage("You can even override preset message colors.", "ERROR", pyconsole.Color.White, pyconsole.Color.Blue)
pyconsole.PrintMessage("You can set the colors for the message and prefix separately.", "Example", pyconsole.Color.BrightCyan, pyconsole.Color.Yellow)
pyconsole.PrintMessage("For even more customizability, you can choose whether to color only the prefix,", "INFO", pyconsole.Color.White, pyconsole.Color.BrightBlue)
pyconsole.PrintMessage("Or the brackets as well.", "INFO", pyconsole.Color.White, pyconsole.Color.BrightBlue, True)
pyconsole.PrintMessage("This message has been logged in the log file.", "INFO", pyconsole.Color.White, pyconsole.Color.White, False, True)
pyconsole.PrintMessage("\n")
pyconsole.UserInput("This is a prompt for input. ")
pyconsole.UserInput("The prompts can be colored. ", pyconsole.Color.BrightYellow)
pyconsole.UserInput("As well as the user's input. ", pyconsole.Color.BrightGreen, pyconsole.Color.Cyan)
pyconsole.UserInput("Press ENTER to exit the program. ")