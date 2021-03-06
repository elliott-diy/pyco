
# pyconsole
`pyconsole` is a Python library designed to help developers make nicer command line applications faster. It has cross-platform compatibility for Windows and Linux and supports color on both as well. There are also numerous small quality of life features that will make your programming easier, such as a built-in error logger and message handler.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `pyconsole`. 
```bash
pip install pyconsole
```

## Usage
### Printing Messages
#### Syntax
`PrintMessage(message, prefix, messageColor, prefixColor, colorBrackets, forceLog)`

Prefixes are automatically enclosed in square brackets.
Certain prefix types like `Error` and `Success` are automatically highlighted in the appropriate color.
You may override preset colors.

#### Parameters
`message` - The message you want to print in the console. Default is `""`.  
`prefix` - The prefix before the message. Default is `"none"`.  
`messageColor` - The color of the message. Default is `pyconsole.Color.White`.  
`prefixColor` - The color of the prefix. Default is `pyconsole.Color.White`.  
`colorBrackets` - Specify whether to color the brackets surrounding the prefix or not. Default is `False`.  
`forceLog` - Force the message to be logged in the log file. Default is `False`.  

#### Examples
##### Code
```python
import pyconsole

PrintMessage("Generic message.")
PrintMessage("Error message.", "Error")
PrintMessage("Warning message.", "Warning")
PrintMessage("Success message.", "Success")
PrintMessage("Info message.", "Info")
PrintMessage("Message in pink.", "none", pyconsole.Color.BrightMagenta)
PrintMessage("Message in blue.", "Green prefix", pyconsole.Color.BrightBlue, pyconsole.Color.Green)
PrintMessage("Message in cyan. The brackets around the prefix are also colored", "Custom Prefix", pyconsole.Color.BrightCyan, pyconsole.Color.Red, True)
PrintMessage("This message has been logged in the log file","Info", None, None, False, True)
```

##### Output
image here

### Input Prompts
#### Syntax
`UserInput(prefix, prefixColor, inputColor)`

#### Parameters
`prefix` - The prompt or question before the user's unput. Default is `""`.  
`prefixColor` - The color of the prefix. Default is `pyconsole.Color.White`.  
`inputColor` - The color of the user's input. Default is `pyconsole.Color.White`.  

#### Examples
##### Code
```python
import pyconsole

UserInput("My prompt.")
UserInput("Prompt in green", pyconsole.Color.Green)
UserInput("Prompt in green, user input  in blue", pyconsole.Color.Green, pyconsole.Color.Blue)
```

##### Output
image here

### Message Prefixes
```pyconsole``` has four premade prefixes that you can use in your program.

#### Examples
##### Code
```python
import pyconsole

print(ConsoleMessage.Success + "Somthing good happend!")
print(ConsoleMessage.Error + "Error 404!")
print(ConsoleMessage.Warning + "Somthing could be broken!")
print(ConsoleMessage.Info + "Heres some info!")
```

##### Output
![Example Image](https://i.imgur.com/CO7ektk.png "Example Image")

### Colors
`pyconsole` has a built-in color system that is designed to be intuitive to use. pyconsole automatically clears the console on Windows consoles to properly display color codes. See the usage below.

#### Normal Colors
```python
import pyconsole

print(pyconsole.Color.Red + "I'm red!")
```

#### Bright Colors
```python
import pyconsole

print(pyconsole.Color.BrightRed + "I'm bright red!")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.

## License
[MIT License](https://choosealicense.com/licenses/mit/)
