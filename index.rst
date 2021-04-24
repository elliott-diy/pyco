
# pyco
By [Duplexes](https://github.com/Duplexes) and [LemonPi314](https://github.com/LemonPi314)

`pyco` is a Python package designed to help developers make better command line applications faster. It has cross-platform compatibility for Windows and Linux. There are also numerous small quality of life features that will make your programming easier, such as a built-in error logger, message handler, progress bars, and a massive list of ANSI escape codes.
## Overview
* [Installation](#installation)
* [Usage](#usage)
    * [Printing Messages](#printing-messages)
    * [User Input](#user-input)
    * [Progress Bars](#progress-bars)
    * [Logging](#logging)
    * [ANSI Escape Codes](#ansi-escape-codes)
* [Additional Resources](#additional-resources)
* [Contributing](#contributing)
* [License](#license)
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `pyco`. 
```bash
pip install pyco
```
## Usage
### Printing Messages
#### Syntax
```python
# Print a message
PrintMessage(message: str, prefix: str, messageColor: Color, prefixColor: Color, colorBrackets: bool, forceLog: bool, sep: str, end: str, flush: bool)
```
Prefixes are automatically enclosed in square brackets.
Certain prefix types like `Error` and `Success` are automatically highlighted in the appropriate color.
You may override preset colors.
#### Parameters
* `message` - The message you want to print in the console. Default is `''`.
* `prefix` - The prefix before the message. Default is `'none'`.
* `messageColor` - The color of the message. Default is `Color.AUTO`.
* `prefixColor` - The color of the prefix. Default is `Color.AUTO`.
* `colorBrackets` - Specify whether to color the brackets surrounding the prefix or not. Default is `False`.
* `forceLog` - Force the message to be logged in the log file. Default is `False`.
* `sep` - Separator, directly passed to `print()`. Default is `' '`.
* `end` - String to print at the end, directly passed to `print()`. Default is `'\n'`.
* `flush` - Flush the output buffer to show changes immediately, directly passed to `print()`. Default is `False`.
### User Input
#### Syntax
```python
# Prompt for user input
UserInput(prefix: str, prefixColor: Color, inputColor: Color)
```
#### Parameters
* `prefix` - The prompt or question before the user's input. Default is `''`.
* `prefixColor` - The color of the prefix. Default is `Color.DEFAULT_PREFIX_COLOR`.
* `inputColor` - The color of the user's input. Default is `Color.DEFAULT_INPUT_COLOR`.
### Progress Bars
#### Syntax
```python
# Create ProgressBar() instance
bar = ProgressBar(total: int, prefix: str, suffix: str, length: int, fill: str, emptyFill: str, decimals: int, end: str, updateIntervalms: int)

# Update the progress bar in a loop
for iteration in range(100):
    bar.Update(iteration)
```
#### Parameters
* `iteration` - The iteration of progress bar (how full it is). Default is `0`.
* `total` - The total number of iterations the progress bar has. Default is `100`.
* `prefix` - The prefix before the progress bar. Default is `''`.
* `suffix` - The suffix after the progress bar. Default is `''`.
* `length` - The number of characters in the progress bar. Default is `100`.
* `fill` - The character to fill the progress bar with. Default is `'█'`.
* `emptyFill` - The character to fill the empty part of the progress bar with. Default is `'-'`.
* `decimals` - The number of decimals to show in the percent. Default is `1`.
* `end` - The character(s) to print at the end. Default is `'\r'`.
### Logging
#### Syntax
```python
# Log a message into a log file
Logger.Log(message: str, prefix: str, prefixBrackets: bool, includeTimestamp: bool)

# Change the log level
Logger.SetLogLevel(level: Levels)

# Clear the log file
Logger.ClearLog()
```
#### Parameters
* `message` - The message of the log entry. Default is `''`.
* `prefix` - The prefix before the message. Default is `''`.
* `includeTimestamp` - Add a timestamp to the entry. Default is `True`.
* `level` - Specify a log level from the list below.
#### Log Levels
* `Logger.Levels.NONE` - Dont log any messages.
* `Logger.Levels.ERROR` - Log errors.
* `Logger.Levels.WARNING` - Log warnings and errors.
* `Logger.Levels.SUCCESS` - Log successes, warnings, and errors.
* `Logger.Levels.INFO` - Log info, successes, warnings, and errors.
* `Logger.Levels.ALL` - Log everything.
#### Variables
You may change these variables at the start of your script.
* `Logger.logPath` - Full path of a text file to log entries into. Default is `'[current working directory]/logs/log.txt'`.
* `Logger.enableMessageLogging` - Enable or disable logging of messages. Default is `True`.
* `Logger.enableInputLogging` - Enable or disable logging of user inputs. Default is `True`.
### ANSI Escape Codes
The `pyco.ansi` class contains ANSI escape codes you can use independently of the `PrintMessage()` and `UserInput()` functions.
#### `ansi.Terminal`
Functions for modifying the terminal window such as `SetTitle()` and `ScrollDown()`.
#### `ansi.Cursor`
Functions for modifying cursor parameters and position, such as `Hide()` and `Down()`.
#### `ansi.Text`
Functions for modifying terminal text through escape codes, such as `DeleteChar()` and `CharSetLineDrawing()`.
#### `ansi.Input`
Functions for emulating keypress events in the terminal such as `RightArrow()` and `F10()`.
#### `ansi.Color`
Color escape code constants and functions. You can combine constants when using them in `PrintMessage()` or `UserInput`, or in other output functions.
```python
PrintMessage("Bright yellow text on a blue background", messageColor=Color.Fore.BRIGHT_YELLOW + Color.Back.BLUE)

print(Color.Style.BOLD + Color.Fore.GREEN + Color.Back.WHITE + "Bold green text on a white background")
```
##### 2-Bit Colors
The original ANSI escape codes for 16 colors (8 normal and 8 bright) can be found as constants under both `Color.Foreground` and `Color.Background` classes.
##### 8-Bit Colors
Most terminals support a palette of 256 colors, accessible with the `EightBit()` function. For a detailed list of colors see <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>.  
`EightBit()` takes one parameter which is the number of the color from `0` to `255`.
##### 24-Bit Colors
Some terminals support standard RGB values like `(53, 174, 89)`, accessible with the `TwentyFourBit()` function.
##### Styles
In addition to colors, there are also style modifiers such as `Color.Style.BOLD` and `Color.Style.UNDERLINE`.
##### Reset
The escape code to reset all color and style modifiers is `Color.Style.RESET`.
##### Defaults
If you wish to change the default message, prefix, or input color used in `PrintMessage()` and `UserInput()`, you can edit `Color.DEFAULT_MESSAGE_COLOR`, `Color.DEFAULT_PREFIX_COLOR`, and `Color.DEFAULT_INPUT_COLOR` to another combination of color codes accordingly.
## Additional Resources
Most of the ANSI escape codes were directly taken from the following two websites:
* <https://en.wikipedia.org/wiki/ANSI_escape_code>
* <https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences>
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## License
[MIT License](https://choosealicense.com/licenses/mit/)
