from pyco import user_input
from pyco.color import Fore, Back, Style

user_input("Plain prompt: ")
user_input(Fore.GREEN + "Prompt in green: ")
user_input(Fore.BRIGHT_RED + "Prompt in bright red, user input in cyan: ", input_color=Fore.CYAN)
user_input(Fore.BLUE + Back.BRIGHT_WHITE + "Prompt in blue on a bright white background, user input in bright magenta with an underline: ", input_color=Fore.BRIGHT_MAGENTA + Style.UNDERLINE)
user_input("This prompt and the following user input has been logged: ", log=True)
