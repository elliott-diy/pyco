# Terminal Printing and Input
## Printing Messages
### Syntax
```python
# Print a message
PrintMessage(message: str, prefix: str, messageColor: Color, prefixColor: Color, colorBrackets: bool, forceLog: bool, sep: str, end: str, flush: bool)
```
Prefixes are automatically enclosed in square brackets.
Certain prefix types like `Error` and `Success` are automatically highlighted in the appropriate color.
You may override preset colors.

### Parameters
- `message` - The message you want to print in the console. Default is `''`.
- `prefix` - The prefix before the message. Default is `'none'`.
- `messageColor` - The color of the message. Default is `Color.AUTO`.
- `prefixColor` - The color of the prefix. Default is `Color.AUTO`.
- `colorBrackets` - Specify whether to color the brackets surrounding the prefix or not. Default is `False`.
- `forceLog` - Force the message to be logged in the log file. Default is `False`.
- `sep` - Separator, directly passed to `print()`. Default is `' '`.
- `end` - String to print at the end, directly passed to `print()`. Default is `'\n'`.
- `flush` - Flush the output buffer to show changes immediately, directly passed to `print()`. Default is `False`.

## User Input
### Syntax
```python
# Prompt for user input
UserInput(prefix: str, prefixColor: Color, inputColor: Color)
```

### Parameters
- `prefix` - The prompt or question before the user's input. Default is `''`.
- `prefixColor` - The color of the prefix. Default is `Color.DEFAULT_PREFIX_COLOR`.
- `inputColor` - The color of the user's input. Default is `Color.DEFAULT_INPUT_COLOR`.
