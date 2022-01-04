import math
import os
import sys
import numpy as np
import sympy as sp
from util import *


cipher = sys.argv[0]
known = sys.argv[1]
location = 0 
n = math.sqrt(len(known))
partial_cipher = cipher[location:location+pow(int(n), 2)]
print(partial_cipher)

cm = tomatrix(partial_cipher, n)
km = tomatrix(known, n)
i = sp.Matrix(cm).inv_mod(26)
d = np.dot(i, km) % 26

print(f"Decryption Key:\n{d}")
#os.system("python decode.py {d} {cipher}")