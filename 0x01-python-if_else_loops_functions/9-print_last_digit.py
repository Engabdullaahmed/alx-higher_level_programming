#!/usr/bin/python3
# Eng,Abdulla


def print_last_digit(number):
    number = abs(number)

    last_digit = number % 10

    print(last_digit, end="")
    return last_digit
