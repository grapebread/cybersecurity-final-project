import sys
import numpy as np

from util import *

key = sys.argv[1]
input = sys.argv[2]
input = input.lower()
mode = sys.argv[3]
mode = mode.lower()
part1 = tonum(key[0]) + 1
part2 = tonum(key[1]) + 1
part3 = tonum(key[2]) + 1
part4 = tonum(key[3]) + 1
key = np.array([[part1, part2],[part3, part4]])
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
            encryptm = encryptm + toletter(encrypted[0]) + toletter(encrypted[1]) 
    return encryptm

print(encode())
