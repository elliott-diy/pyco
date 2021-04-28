# Progress Bars
## Syntax
```python
# Create ProgressBar() instance
bar = ProgressBar(total: int, prefix: str, suffix: str, length: int, fill: str, emptyFill: str, decimals: int, end: str, updateIntervalms: int)
# Update the progress bar in a loop
for iteration in range(100):
    bar.Update(iteration)
```

## Parameters
- `iteration` - The iteration of progress bar (how full it is). Default is `0`.
- `total` - The total number of iterations the progress bar has. Default is `100`.
- `prefix` - The prefix before the progress bar. Default is `''`.
- `suffix` - The suffix after the progress bar. Default is `''`.
- `length` - The number of characters in the progress bar. Default is `100`.
- `fill` - The character to fill the progress bar with. Default is `'█'`.
- `emptyFill` - The character to fill the empty part of the progress bar with. Default is `'-'`.
- `decimals` - The number of decimals to show in the percent. Default is `1`.
- `end` - The character(s) to print at the end. Default is `'\r'`.
