import math
import sys
import numpy as np

from util import *

key = sys.argv[1]
input = sys.argv[2]
input = input.lower()
n = math.sqrt(len(key))
key = tomatrix(key, int(n))
KEYrows = key.shape[0]

def encrypt(messageToEncode, key): 
    encryption = key @ messageToEncode 
    encryption = np.remainder(encryption, 26) 
    return encryption

def encode():
    messageToEncode = tomatrix(input, KEYrows) 
    encryptm = "" 
    for i in range(0, len(messageToEncode)):
        encrypted = encrypt(messageToEncode[i], key) 
        for c in encrypted:
            encryptm += toletter(c)
    return encryptm

print(encode().upper())