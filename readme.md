# PythonTools
Some useful functions and color codes for Python console programming.
## Functions
### ```PrintMessage(message, prefix, forceColor, colorMessage, forceLog)```
Print a message with color and a customizable prefix. Includes an option to log the message,  
and an option whether to color the whole message or just the prefix.
### ```UserInput(prefix, prefixColor, inputColor)```
Print a prompt with color and ask for input from the user.  
Options to set colors for the prefix and input separately.
### ```Logger(message, prefix)```
Log a message into a log file. Done automatically for errors and warnings.
### ```ClearLog()```
Clear the log file to save some disk space. The log file is cleared automatically when the script starts.
## Color Codes
```Python
Black = "\u001b[30m"    
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta =  "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m"
BrightBlack = "\u001b[30;1m"
BrightRed = "\u001b[31;1m"
BrightGreen = "\u001b[32;1m"
BrightYellow = "\u001b[33;1m"
BrightBlue = "\u001b[34;1m"
BrightMagenta = "\u001b[35;1m"
BrightCyan = "\u001b[36;1m"
BrightWhite = "\u001b[37;1m"
```
## License
[MIT License](https://choosealicense.com/licenses/mit/)
