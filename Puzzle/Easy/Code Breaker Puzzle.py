import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

alphabet = input()
message = input()
word = input()


def decode(c, a, b):
    m1 = c * b
    m2 = m1 % len(alphabet)
    m3 = m2 - a
    return m3


def decode_message(message, a, b):
    tmp_decode = ""
    for c in message:
        i = decode(alphabet.index(c), a, b)
        tmp_decode += alphabet[i]

    return tmp_decode


def solution():
    for a in range(len(alphabet)):
        for b in range(1, len(alphabet)):
            tmp = decode_message(message, a, b)
            if word in tmp:
                return tmp


print(solution())
