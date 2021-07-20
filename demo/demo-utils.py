from pyco.utils import kbhit, getch
import time

print("Press any key:")
counter = 0
while True:
    if kbhit():
        print(f"You pressed: {getch()}\tCounter is at: {counter}")
    counter += 1
    time.sleep(1)
