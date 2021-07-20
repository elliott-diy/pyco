# Pyco
Created by [Duplexes](https://github.com/Duplexes) and [LemonPi314](https://github.com/LemonPi314)

Pyco is a Python package designed to help developers make better command line applications faster. It has cross-platform compatibility for Windows and Linux. Some of the included features are a built-in error logger, colorized terminal input and output, progress bars, and an extensive list of ANSI escape code functions.  
Full documentation can be found at <https://duplexes.me/pyco>.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pyco. 
```bash
pip install pyco
```

## Usage
Basic usage of included functions and constants.
```python
from pyco import *
from pyco.color import Fore, Back
# Print a message with a prefix
print_message("message", "prefix")
# Print a message with color
print_message(Fore.RED + "message")
# Print a message with a prefix and color
print_message(Fore.BRIGHT_YELLOW + "message", prefix=Fore.BLUE + "prefix")
# Prompt for user input with color
user_input(Back.GREEN + "prompt", input_color=Fore.BRIGHT_WHITE)
# Log a message into a log file
logging.log("message", "prefix")
```

## Contributing
This project is a work-in-progress, so any issues and bug reports are greatly appreciated. Pull requests are welcome. For major changes and feature requests, please [open an issue](https://github.com/Duplexes/pyco/issues/new) first to discuss what you would like to change.

## License
[MIT License](https://choosealicense.com/licenses/mit/)
