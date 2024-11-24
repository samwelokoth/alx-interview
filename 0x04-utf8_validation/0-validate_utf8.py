#!/usr/bin/python3
"""
"""

def validUTF8(data):
    list = []
    for i in data:
        if (i & 0xF0) == 0xF0:
            list.append(4)
        if (i & 0xE0) == 0xE0:
            list.append(3)
        if (i & 0xC0) == 0xC0:
            list.append(2)
        if (i & 0x7F) == 0:
            list.append(1)
    print(list)


data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
validUTF8(data)
