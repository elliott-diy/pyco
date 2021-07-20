from pyco import print_message
from pyco.color import Fore, Back, Style, RESET
from pyco import prefix

print_message("This is a normal message")
print_message("This is an error message", prefix=prefix.ERROR)
print_message("This is a warning message", prefix=prefix.WARNING)
print_message("This is a success message", prefix=prefix.SUCCESS)
print_message("This is an info message", prefix=prefix.INFO)
print_message("This is a message with a custom prefix", prefix="Custom Prefix:")
print_message(Fore.BRIGHT_CYAN + "This is a message with a custom color")
print_message(Fore.BRIGHT_MAGENTA + "You can combine custom prefixes and colors", prefix="Example:")
print_message(Fore.RED + "You can set the colors for the message and prefix separately", prefix=Fore.YELLOW + "Example:")
prefix.ERROR = f"{Fore.GREEN}[ERROR]{RESET}"
print_message("You can edit default prefixes at runtime", prefix=prefix.ERROR)
print_message("This message has been logged in the log file", prefix=prefix.INFO, log=True)
