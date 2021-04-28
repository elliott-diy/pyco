# ANSI Escape Codes
The `pyco.ansi` class contains ANSI escape codes you can use independently of the `PrintMessage()` and `UserInput()` functions.

## Terminal
Functions for modifying the terminal window such as `SetTitle()` and `ScrollDown()`.

## Cursor
Functions for modifying cursor parameters and position, such as `Hide()` and `Down()`.

## Text
Functions for modifying terminal text through escape codes, such as `DeleteChar()` and `CharSetLineDrawing()`.

## Input
Functions for emulating keypress events in the terminal such as `RightArrow()` and `F10()`.

## Color
Color escape code constants and functions. You can combine constants when using them in `PrintMessage()` or `UserInput`, or in other output functions.
```python
PrintMessage("Bright yellow text on a blue background", messageColor=Color.Fore.BRIGHT_YELLOW + Color.Back.BLUE)
print(Color.Style.BOLD + Color.Fore.GREEN + Color.Back.WHITE + "Bold green text on a white background")
```

### 4-Bit Colors
The original ANSI escape codes for 16 colors (8 normal and 8 bright) can be found as constants under both `Color.Foreground` and `Color.Background` classes.

### 8-Bit Colors
Most terminals support a palette of 256 colors, accessible with the `EightBit()` function. For a detailed list of colors see <https://en.wikipedia.org/wiki/ANSI_escape_code#8-bit>.

`EightBit()` takes one parameter which is the number of the color from `0` to `255`.
### 24-Bit Colors
Some terminals support standard RGB values like `(53, 174, 89)`, accessible with the `TwentyFourBit()` function.

### Styles
In addition to colors, there are also style modifiers such as `Color.Style.BOLD` and `Color.Style.UNDERLINE`.

### Reset
The escape code to reset all color and style modifiers is `Color.Style.RESET`.

### Defaults
If you wish to change the default message, prefix, or input color used in `PrintMessage()` and `UserInput()`, you can edit `Color.DEFAULT_MESSAGE_COLOR`, `Color.DEFAULT_PREFIX_COLOR`, and `Color.DEFAULT_INPUT_COLOR` to another combination of color codes accordingly.
