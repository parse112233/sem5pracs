#Vernam Cipher

import string
from random import shuffle
def encrypt(pt, key):
    if len(key) != len(pt):
        raise ValueError("Plain text should be the same length as the key")

    cipher = ""
    pt_list = list(pt)
    pool = list(string.ascii_lowercase)
    for i in range(0, len(pt)):
        alpha1 = ord(pt_list[i])
        alpha2 = ord(key[i])

        xor = alpha1 ^ alpha2
        if xor > 25:
            xor = xor - 25

        cipher += (pool[xor])
    return cipher

def encrypts(pt, key):
    if len(key) != len(pt):
        raise ValueError("Plain text should be the same length as the key")

    cipher = ""
    pool = list(string.ascii_lowercase)
    for i in range(0, len(pt)):
        p = pool.index(pt[i].lower())
        k = pool.index(key[i].lower())
        c = p ^ k

        if c >= 26:
            c = c - 26
        cipher += pool[c]
    return cipher

# print(encrypt("abc", "xyz"))
print(encrypts("hello", "world"))












