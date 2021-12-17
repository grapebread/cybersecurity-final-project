# Manual implementation for testing known-plaintext attacks

from functools import partial
import numpy as np
import sympy as sp
import os
from util import *

"""
cipher = "fupcmtgzkyukbqfjhuktzkkixtta"
known = "ofthe"

def matrix_to_str(matrix):
    s = ""
    for i in matrix:
        for j in i:
            s += chr(j + 97)

    return s

cm = [tonum(n) for n in cipher]
m = tomatrix(cipher, 2)
km = [tonum(n) for n in known]

inverted = []
for i in range(len(km) - 3):
    kt = np.array(km[i:i+4])
    kt.resize(2, 2)

    for i in range(len(cm) - 3):
        ct = np.array(cm[i:i+4])
        ct.resize(2,2)

        try:
            temp = inv(ct @ inv(kt))
            print(temp)
            inverted.append(temp)
        except:
            pass


for n in inverted:
    key = matrix_to_str(n)
    print(os.system(f"python decode.py {key} {cipher}"))
"""

cipher = "fupcmtgzkyukbqfjhuktzkkixtta"
known = "fthe"
location = 18
partial_cipher = cipher[location:location+len(known)]
print(partial_cipher)

cm = tomatrix(partial_cipher, 2)
km = tomatrix(known, 2)
i = sp.Matrix(cm).inv_mod(26)
d = np.dot(i, km) % 26

print(f"cipher:{cm}")
print(f"known:{km}")
print(f"inv:{i}")
print(f"d:{d}")

#print(os.system(f"python decode.py"))