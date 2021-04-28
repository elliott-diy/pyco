# Logging
## Syntax
```python
# Log a message into a log file
Logger.Log(message: str, prefix: str, prefixBrackets: bool, includeTimestamp: bool)
# Change the log level
Logger.SetLogLevel(level: Levels)
# Clear the log file
Logger.ClearLog()
```

## Parameters
- `message` - The message of the log entry. Default is `''`.
- `prefix` - The prefix before the message. Default is `''`.
- `includeTimestamp` - Add a timestamp to the entry. Default is `True`.
- `level` - Specify a log level from the list below.

## Log Levels
- `Logger.Levels.NONE` - Dont log any messages.
- `Logger.Levels.ERROR` - Log errors.
- `Logger.Levels.WARNING` - Log warnings and errors.
- `Logger.Levels.SUCCESS` - Log successes, warnings, and errors.
- `Logger.Levels.INFO` - Log info, successes, warnings, and errors.
- `Logger.Levels.ALL` - Log everything.

## Variables
You may change these variables at the start of your script.
- `Logger.logPath` - Full path of a text file to log entries into. Default is `'[current working directory]/logs/log.txt'`.
- `Logger.enableMessageLogging` - Enable or disable logging of messages. Default is `True`.
- `Logger.enableInputLogging` - Enable or disable logging of user inputs. Default is `True`.
