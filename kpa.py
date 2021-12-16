# Manual implementation for testing known-plaintext attacks

import numpy as np
from util import *

cipher = "fupcmtgzkyukbqfjhuktzkkixtta"
known = "ofthe"

cm = [tonum(n) for n in cipher]
km = [tonum(n) for n in known]

for i in range(len(km) - 3):
    kt = np.array(km[i:i+4])
    kt.resize(2, 2)

    for i in range(len(cm) - 3):
        ct = np.array(cm[i:i+4])
        ct.resize(2,2)

        inverted = []
        print(ct)
        try:
            inverted = inv(ct)
            print(inverted)
            print()
        except:
            print("inversion failed")

a = np.array([[15,2],[12,19]])
inv(a)