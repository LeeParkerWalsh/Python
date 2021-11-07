import sys


def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1


print('Enter number:')
try:
    value = int(input())
except ValueError:
    print('Please enter an integer')
    sys.exit()
while value > 1:
    value = collatz(value)
    print(value)
