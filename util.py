import string
import numpy as np

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

def tonum(letter):
    return string.ascii_lowercase.index(letter) - 1 

def toletter(ascii):
    return chr(int(ascii) + 97) 