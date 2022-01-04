import math
import os
import sys
import numpy as np
import sympy as sp
from util import *


cipher = "".join([n for n in sys.argv[1].lower() if n.isalpha()])
known = "".join([n for n in sys.argv[2].lower() if n.isalpha()])
location = int(sys.argv[3])
n = math.sqrt(len(known))
partial_cipher = cipher[location:location+pow(int(n), 2)]
print(partial_cipher)

cm = tomatrix(partial_cipher, int(n))
km = tomatrix(known, int(n))
i = sp.Matrix(cm).inv_mod(26)
d = np.dot(i, km) % 26

dkey = ""
for row in d.T:
    for col in row:
        dkey += toletter(col)


print(f"Key: {dkey}")
print("Now you can encode the enciphered text using this key to get the original message!")