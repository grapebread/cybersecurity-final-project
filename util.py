import string
import numpy as np

def tomatrix(input, key_rows): 
    message = []
    for i in range(0, len(input)):
        current_letter = (input[i:i+1]).lower()
        if current_letter != ' ': 
            letter_index = tonum(current_letter) 
            message.append(letter_index)
    while (len(message) % key_rows != 0): message.append(0)
    message = np.array(message) 
    message_length = message.shape[0]
    message.resize(int(message_length/key_rows), key_rows)
    return message

def tonum(letter):
    return string.ascii_lowercase.index(letter) 

def toletter(ascii):
    return chr(int(ascii) + 97) 

"""
returns the inverse of the matrix parameter in mod 26
matrix represents some invertible matrix (square numpy array with a non-zero determinant)
"""
def inv(matrix):
    det = round(np.linalg.det(matrix))
    x = pow(det, -1, 26)

    adj = [[matrix[1][1], -1 * matrix[0][1]], [-1 * matrix[1][0], matrix[0][0]]]
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            adj[i][j] *= x
            adj[i][j] %= 26

    return adj