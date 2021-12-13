import sys
import numpy as np

from util import *

key = sys.argv[1]
input = sys.argv[2]
input = input.lower()
mode = sys.argv[3]
mode = mode.lower()
key_rows = key.shape[0]

def encrypt(message, key): 
    encryption = key @ message 
    encryption = np.remainder(encryption, 26) 
    return encryption

def encode():
    message = tomatrix(input, key_rows) 
    encryptm = "" 
    for i in range(0, len(message)):
            encrypted = encrypt(message[i], key) 
            encryptm = encryptm + toletter(encrypted[0]) + toletter(encrypted[1]) 
    return encryptm
