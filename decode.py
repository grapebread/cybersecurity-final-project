import sys
import math
import numpy as np

from util import *

# Note this is only for the 2x2 case

"""
if n is an int, return corresponding char
if n is a char, return corresponding int
"""
def convert(n):
    if type(n) == int:
        return chr(n + 97)
    elif type(n) == str:
        return ord(n.lower()) - 97

"""
cipher_matrix is a n-component vector (i.e [1, 2, 3, 4, 5])
key is a square matrix (i.e [[1, 2], [3, 4]] where the number of elements
must be a perfect square)
key must also be an invertible matrix (hence have a zero determinant)
"""
def decode(cipher_matrix, inverted_key):
    plain_matrix = []
    #inverted_key = inv(key)

    for n in cipher_matrix:
        temp = inverted_key @ n
        for x in temp: plain_matrix.append(x % 26)

    return plain_matrix

if len(sys.argv) < 3:
    print("Example for input: python decode.py \"key\" \"ciphertext\"")
    exit()

ciphertext = sys.argv[2]
clean_ciphertext = "".join(ciphertext.lower().split())
key = "".join(sys.argv[1].lower().split())

n = math.sqrt(len(key))
if int(n) != n:
    print("Key is not a square matrix")
    exit()

cipher_matrix = tomatrix(ciphertext, int(n))
key_matrix = tomatrix(key, int(n))

inverted = []
try:
    inverted = inv(key_matrix)
except:
    print("Key matrix is not invertible mod 26")
    exit()

plain_matrix = decode(cipher_matrix, inverted)

plaintext = ""
for n in plain_matrix[:len(ciphertext)]:
    plaintext += toletter(n)

print(plaintext)