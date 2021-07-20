# Pyco
Created by [Duplexes](https://github.com/Duplexes) and [LemonPi314](https://github.com/LemonPi314)

Pyco is a Python package designed to help developers make better command line applications faster. It has cross-platform compatibility for Windows and Linux. Some of the included features are a built-in error logger, colorized terminal input and output, progress bars, and an extensive list of ANSI escape code functions.

## Overview
- [Installation](#installation)
- [Terminal IO](terminal-io.md)
- [Progress Bars](progress-bars.md)
- [Logging](logging.md)
- [ANSI Escape Codes](ansi.md)
- [Additional Resources](#additional-resources)
- [Contributing](#contributing)
- [License](#license)

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Pyco. 
```bash
pip install pyco
```

## Roadmap
Features and tasks for the future.

- [ ] Add `sys.stdout` wrapper for automatic color reset
- [ ] Add `typewrite()` function
- [ ] Add `Indicator` progress bar type
- [ ] Customizable progress bar styles
- [ ] Add list of pre-made prefixes
- [ ] Expand list of functions and ANSI constants
- [ ] Rewrite documentation
- [ ] Clean imported module namespaces (possibly)

## Additional Resources
Most of the ANSI escape codes were sourced from the following websites:
- <https://en.wikipedia.org/wiki/ANSI_escape_code>
- <https://docs.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences>

## Contributing
This project is a work-in-progress, so any issues and bug reports are greatly appreciated. Pull requests are welcome. For major changes and feature requests, please [open an issue](https://github.com/Duplexes/pyco/issues/new) first to discuss what you would like to change.

## License
[MIT License](https://choosealicense.com/licenses/mit/)
