# Logging
The `Logger` class contains methods and constants for logging entries into a log file. The logger is integrated with [`print_message()`] and [`user_input()`].

## Variables
Change these variables at the start of your script to alter the behavior of the logger.

Variable|Default Value|Type|Description
----------------------|----------------------|-------|--------------------------------------------
`logPath`             |`'[cwd]/logs/log.txt'` |`str`  |Full path of a text file to log entries into
`enableMessageLogging`|`False`                |`bool` |Enable or disable logging of messages
`enableInputLogging`  |`False`                |`bool` |Enable or disable logging of user inputs
`enableTimestamp`     |`True`                 |`bool` |Enable or disable timestamps in log entries
`timestampFormat`     |`'%Y-%m-%d %H:%M:%S%z'`|`str`  |Timestamp format as a [`datetime.datetime.strftime()`](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) format string
`logLevel`            |`Levels.ERROR`         |`int`  |Log level

## Logging Messages
Use `Log()` to log a message into the log file specified by `logPath`.

Parameter|Default Value|Type|Description
------------------|------|------|-----------------------------
`message`         |`''`  |`str` |The message of the log entry
`prefix`          |`''`  |`str` |The prefix before the message

### Alternate Names
- `log()`

## Set Log Level
Use `SetLogLevel()` to set the log level using a constant from the `Levels` class, or a string or integer corresponding to a constant in the `Levels` class. You can also simply set the `logLevel` variable to a constant from the `Levels` class.

Parameter|Type|Description
-------|-------|---------------------------------
`level`|`Level`|Log level from the `Levels` class

### Alternate Names
- `set_log_level()`
- `SetLevel()`
- `set_level()`

## Clear Log
Use `ClearLog()` to clear the log file. The log file does not get deleted.

### Alternate Names
- `clear_log()`

## Log Levels
Level|Value|Description
----------------|---|-----------------------------------------
`Levels.NONE`   |`0`|Dont log any messages
`Levels.ERROR`  |`1`|Log errors
`Levels.WARNING`|`2`|Log warnings and errors
`Levels.SUCCESS`|`3`|Log successes, warnings, and errors
`Levels.INFO`   |`4`|Log info, successes, warnings, and errors
`Levels.ALL`    |`5`|Log everything

### Alternate Names
- `levels`
- `LogLevels`
- `log_levels`

## Example
<details>
<summary>Click to expand</summary>

### `demo-logging.py`
```python
from pyco import *

Logger.ClearLog()
Logger.enableMessageLogging = True
Logger.Log("Log file gets created automatically", "[Prefix]")
print_message("Error messages logged by default", "[ERROR]")
Logger.Log("Log entry without a prefix")
Logger.enableInputLogging = True
user_input("Input logging enabled: ")
Logger.SetLogLevel(Logger.Levels.ALL)
print_message("Log level set to 'ALL'", "[Prefix]")
```

### `log.txt`
```log
[2021-05-13 00:21:29-0000] [INFO] Cleared log file contents
[2021-05-13 00:21:29-0000] [Prefix] Log file gets created automatically
[2021-05-13 00:21:29-0000] [ERROR] Error messages logged by default
[2021-05-13 00:21:29-0000] Log entry without a prefix
[2021-05-13 00:21:30-0000] Input logging enabled: input
[2021-05-13 00:21:30-0000] [Prefix] Log level set to 'ALL'
```
</details>

[`print_message()`]: terminal-io.md#printing-messages
[`user_input()`]: terminal-io.md#user-input
