#                  __ _
#                 / _(_)
#  _ __  _ __ ___| |_ ___  __
# | '_ \| '__/ _ \  _| \ \/ /
# | |_) | | |  __/ | | |>  <
# | .__/|_|  \___|_| |_/_/\_\
# | |
# |_|

"""Default prefixes for `print_message()`."""

from . import color as _color

ERROR = f'{_color.DEFAULT_MESSAGE_COLOR}[{_color.ERROR}ERROR{_color.DEFAULT_MESSAGE_COLOR}]{_color.RESET}'
WARNING = f'{_color.DEFAULT_MESSAGE_COLOR}[{_color.WARNING}WARNING{_color.DEFAULT_MESSAGE_COLOR}]{_color.RESET}'
SUCCESS = f'{_color.DEFAULT_MESSAGE_COLOR}[{_color.SUCCESS}SUCCESS{_color.DEFAULT_MESSAGE_COLOR}]{_color.RESET}'
INFO = f'{_color.DEFAULT_MESSAGE_COLOR}[{_color.INFO}INFO{_color.DEFAULT_MESSAGE_COLOR}]{_color.RESET}'
