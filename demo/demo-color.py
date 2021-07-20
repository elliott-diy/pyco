from pyco.color import Fore, Back, Style

print(Fore.DEFAULT + Back.DEFAULT + "Plain text with default colors" + Style.RESET)
print(Fore.RED + Back.BRIGHT_YELLOW + "Dark red text on a bright yellow background" + Style.RESET)
print(Fore.BRIGHT_GREEN + "Bright green text")
print("Text is still bright green" + Style.RESET)
print("Reset back to default colors")
print(Style.BOLD + Fore.CYAN + "Bold cyan text" + Style.RESET)
print(Style.INVERT + "Foreground and background colors inverted" + Style.RESET)
print(Fore.EightBit(208) + "Color value '208' from the 256-color palette" + Style.RESET)
print(Fore.twenty_four_bit((164, 43, 202)) + "Purple text from RGB value" + Style.RESET)
print(Fore.twenty_four_bit('#f7346e') + "Pink-red text from HEX value" + Style.RESET)
print(Style.BOLD + Style.UNDERLINE + Fore.twenty_four_bit((47, 237, 202)) + Back.twenty_four_bit((138, 92, 92)) + "Bold underlined teal text on a red-gray background" + Style.RESET)
