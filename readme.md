# Py-Console

Py-Console is a python library designed to help developers make nicer command line applications faster. It has cross-platform compatibility(Hopefully!) for Windows and Linux and supports color on both as well. There are also numerous small quality of life features that will make your programming easier, such as a built-in error logger and message handler.
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Py-Console. 

```bash
pip install Py-Console
```

## Usage
###Message Handler
###Message Prefixes
Py-Console has four premade prefixes that you can use in your program. The usage is below and what it looks like in the console are below.
```python
import Py-Console

print(ConsoleMessage.Warning + "Somthing could be broken!")
print(ConsoleMessage.Error + "Error 404!")
print(ConsoleMessage.Info + "Heres some info!")
print(ConsoleMessage.Success + "Somthing good happend!")
```
#### What it looks like
![Example Image](https://i.imgur.com/CO7ektk.png "Example Image")
###Colors
Py-Console has a built-in color system that is designed to be intuitive to use. Py-Console automatically clears the console on Windows consoles to properly display color codes. See the usage below.

####Normal Colors
```python
import Py-Console

print(ConsoleColor.Red + "I'm red!")
```
####Bright Colors
```python
import Py-Console

print(ConsoleColor.BrightRed + "I'm bright red!")
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
