#!/usr/bin/python3
# Eng, Abdulla


for num in range(0, 100):
    if num == 99:
        print(f"{num}")
    else:
        print("{:02}".format(num), end=", ")
