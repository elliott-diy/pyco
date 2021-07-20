from pyco import NonBlockingInput
from pyco.color import Fore
import time


def my_callback(data):
    print(f"You entered: {data}\tCounter is at: {counter}")


input_thread = NonBlockingInput(prefix=Fore.BRIGHT_YELLOW + 'Non-blocking input: ', callback=my_callback)
input_thread.start()
counter = 0
for i in range(50):
    counter += 1
    time.sleep(0.5)
input_thread.stop()
print("\nInput thread stopped.")
