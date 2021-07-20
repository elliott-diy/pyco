from pyco import print_message, user_input, logging
from pyco.color import Fore

logging.clear_log()
logging.enable_message_logging = True
logging.log("Log file gets created automatically", "[Prefix]")
print_message("Error messages logged by default", "[ERROR]")
logging.log("Log entry without a prefix")
logging.enable_input_logging = True
user_input("Input logging enabled: ")
logging.set_log_level(logging.Levels.ALL)
print_message("Log level set to 'ALL'", "[Prefix]")
print_message(Fore.BRIGHT_CYAN + "Escape codes in messages are automatically removed.", Fore.BRIGHT_MAGENTA + "Colorized Prefix:")
