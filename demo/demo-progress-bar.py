from pyco.progress import ProgressBar
import time

bar = ProgressBar(prefix="Example progress bar")
for i in range(51):
    bar.update(i)
    time.sleep(0.1)
