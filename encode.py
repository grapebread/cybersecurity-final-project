import math
import sys
import string
import numpy as np

from sympy import Matrix

key = sys.argv[1]
input = sys.argv[2]
input = input.lower()
mode = sys.argv[3]
mode = mode.lower()
key_rows = key.shape[0]

def tonum(letter):
    return string.ascii_lowercase.index(letter) - 1 

def toletter(ascii):
    return chr(int(ascii) + 97) 

def encrypt(message, key): 
    encryption = key @ message 
    encryption = np.remainder(encryption, 26) 
    return encryption

def tomatrix(input, key_rows): 
    message = []
    for i in range(0, len(input)):
        current_letter = (input[i:i+1]).lower()
        if current_letter != ' ': 
            letter_index = tonum(current_letter) 
            message.append(letter_index + 1)
    message = np.array(message) 
    message_length = message.shape[0]
    message.resize(int(message_length/key_rows), key_rows)
    return message

def encode():
    message = tomatrix(input, key_rows) 
    encryptm = "" 
    for i in range(0, len(message)):
            encrypted = encrypt(message[i], key) 
            encryptm = encryptm + toletter(encrypted[0]) + toletter(encrypted[1]) 
    return encryptm
