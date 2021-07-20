#  _ __  _   _  ___ ___
# | '_ \| | | |/ __/ _ \
# | |_) | |_| | (_| (_) |
# | .__/ \__, |\___\___/
# | |     __/ |
# |_|    |___/

"""Terminal input/output."""

from threading import Thread as _Thread
from . import color, logging
from . import prefix as _prefix
from .utils import remove_ansi as _remove_ansi


def print_message(message: str = '', prefix: str = '', log: bool = None, end: str = '\n', flush: bool = False):
    """
    A replacement for `print()` with color and various prefix and logging options.

    Parameters:\n
        `message` - The message you want to print.\n
        `prefix` - The prefix before the message.\n
        `log` - Force the message to be logged regardless of the prefix.\n
        `end` - String to print at the end, passed directly to `print()`.\n
        `flush` - Flush the output buffer, passed directly to `print()`.
    """
    message = str(message) if message is not None else ''
    prefix = str(prefix) if prefix is not None else ''
    if prefix != '' and prefix[-1] != ' ':
        prefix = prefix + ' '
    auto_log = False
    if prefix == _prefix.ERROR:
        if logging.log_level >= logging.Levels.ERROR:
            auto_log = True
    elif prefix == _prefix.WARNING:
        if logging.log_level >= logging.Levels.WARNING:
            auto_log = True
    elif prefix == _prefix.SUCCESS:
        if logging.log_level >= logging.Levels.SUCCESS:
            auto_log = True
    elif prefix == _prefix.INFO:
        if logging.log_level >= logging.Levels.INFO:
            auto_log = True
    if logging.log_level == logging.Levels.ALL:
        auto_log = True
    if log is not None:
        auto_log = log
    if (auto_log and logging.enable_message_logging) or log:
        logging.log(message, prefix)
    print(f'{color.RESET}{color.DEFAULT_PREFIX_COLOR}{prefix}{color.RESET}{color.DEFAULT_MESSAGE_COLOR}{message}{color.RESET}', end=end, flush=flush)


def user_input(prefix: str = '', input_color: color = None, log: bool = None) -> str:
    """
    Prompt for user input with colors and logging.

    Parameters:\n
        `prefix` - The prompt before user's input.\n
        `input_color` - The color of the user's input.\n
        `log` - Force the prefix and input to be logged.
    """
    prefix = str(prefix) if prefix is not None else ''
    input_color = color.DEFAULT_INPUT_COLOR if input_color is None else input_color
    input_string = input(f'{color.RESET}{color.DEFAULT_PREFIX_COLOR}{prefix}{color.RESET}{input_color}')
    print(color.RESET, end='')
    if (logging.enable_input_logging and log is not False) or log:
        logging.log(input_string, prefix)
    return input_string


class NonBlockingInput(_Thread):
    def __init__(self, callback = None, name: str = 'NonBlockingInputThread', daemon: bool = True, **kwargs):
        """
        Threaded non-blocking input.

        Parameters:\n
            `callback` - The function to call when input is received.\n
            `name` - The name of the input thread.\n
            `daemon` - Run as a daemon thread.\n
        """
        kwargs.setdefault('prefix', '')
        kwargs.setdefault('input_color', None)
        kwargs.setdefault('log', None)
        self.kwargs = kwargs
        if callback is None:
            callback = self.get

        self.callback = callback
        self.input = None
        self.stopped = False
        super(NonBlockingInput, self).__init__(name=name, daemon=daemon, target=self.run)

    def run(self):
        while not self.stopped:
            self.input = user_input(**self.kwargs)
            self.callback(self.input)

    def stop(self):
        self.stopped = True

    def get(self):
        return self.input
