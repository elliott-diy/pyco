#  _ __  _ __ ___   __ _ _ __ ___  ___ ___
# | '_ \| '__/ _ \ / _` | '__/ _ \/ __/ __|
# | |_) | | | (_) | (_| | | |  __/\__ \__ \
# | .__/|_|  \___/ \__, |_|  \___||___/___/
# | |               __/ |
# |_|              |___/

"""Terminal progress bar class."""

import time as _time


class ProgressBar:
    def __init__(self, iteration: int = 0, total: int = 50, prefix: str = '', suffix: str = '', length: int = 50, fill: str = '█', empty_fill: str = '-', decimals: int = 1, end: str = '\r', update_interval: float = 100):
        """
        Create an instance of this class to create a progress bar in the console using `bar = ProgressBar()`.
        To update the progress bar call `bar.update(counter)` in a loop where `counter` is increased every iteration.

        Parameters:\n
            `iteration` - Current iteration.\n
            `total` - Total iterations.\n
            `prefix` - Prefix string.\n
            `suffix` - Suffix string.\n
            `length` - Character length of bar.\n
            `fill` - Bar fill character.\n
            `empty_fill` - Character to fill in empty part of the bar.\n
            `decimals` - Positive number of decimals in percent complete.\n
            `end` - End character (e.g. `'\\r'`, `'\\r\\n'`).\n
            `update_interval` - Progress bar will not update if less than this number of milliseconds has passed
        """
        self.iteration = iteration
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.length = length
        self.fill = fill
        self.empty_fill = empty_fill
        self.decimals = decimals
        self.end = end
        self.update_interval = update_interval
        self.last_update_time = 0

    def update(self, iteration: int = None, force: bool = False, **kwargs):
        now = _time.perf_counter()
        kwargs.setdefault('total', self.total)
        kwargs.setdefault('prefix', self.prefix)
        kwargs.setdefault('suffix', self.suffix)
        kwargs.setdefault('length', self.length)
        kwargs.setdefault('fill', self.fill)
        kwargs.setdefault('empty_fill', self.empty_fill)
        kwargs.setdefault('decimals', self.decimals)
        kwargs.setdefault('end', self.end)
        kwargs.setdefault('update_interval', self.update_interval)
        self.iteration = iteration
        self.total = kwargs['total']
        self.prefix = kwargs['prefix']
        self.suffix = kwargs['suffix']
        self.length = kwargs['length']
        self.fill = kwargs['fill']
        self.empty_fill = kwargs['empty_fill']
        self.decimals = kwargs['decimals']
        self.end = kwargs['end']
        self.update_interval = kwargs['update_interval']
        if iteration is not None:
            self.iteration = iteration

        if self.update_interval == 0:
            self.update_interval = 1

        if force is False and self.iteration < self.total and (now - self.last_update_time) < (self.update_interval / 1000):
            return

        self.last_update_time = now
        ProgressBar._print_progress_bar(iteration=self.iteration, total=self.total, prefix=self.prefix, suffix=self.suffix, length=self.length, fill=self.fill, empty_fill=self.empty_fill, decimals=self.decimals, end=self.end)
        if self.iteration == self.total:
            print()

    def increment(self, force: bool = False, **kwargs):
        self.update(self.iteration, force, **kwargs)
        self.iteration += 1

    @staticmethod
    def _print_progress_bar(iteration, total, prefix, suffix, length, fill, empty_fill, decimals, end):
        percent = f'{round(100 * (iteration / total), int(decimals))}'
        filled_length = int(length * iteration // total)
        bar = (fill * filled_length) + (empty_fill * (length - filled_length))
        print(f'{prefix} |{bar}| {percent}% {suffix}', end=end, flush=True)


#class ProgressIndicator:
#    pass
