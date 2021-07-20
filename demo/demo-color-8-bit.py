from pyco.color import Fore, Back, Style

for code in range(256):
    print(f"{Fore.EightBit(code)} {str(code).ljust(4)}", end='')
    if code % 16 == 15:
        print(Style.RESET)
print()
for code in range(256):
    print(f"{Back.EightBit(code)} {str(code).ljust(4)}", end='')
    if code % 16 == 15:
        print(Style.RESET)
