#!/usr/bin/python3
# Eng,Abdulla

def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    before = str[:n]
    after  = str[n+1:]
    return before + after 
