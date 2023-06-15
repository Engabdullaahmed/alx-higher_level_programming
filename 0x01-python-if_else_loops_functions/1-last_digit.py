#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = -last
print("last digit of {} is {} and is ".format(number, last), end="")
if last == 0:
    print("0")
elif last > 5:
    print("greater than 5")
else:
    print("less than 6 and not 0")
