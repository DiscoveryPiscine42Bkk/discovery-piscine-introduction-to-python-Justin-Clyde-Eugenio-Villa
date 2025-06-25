#!/usr/bin/env python3

import sys

param = sys.argv
param_count = len(sys.argv) -1

if param_count > 0:
    for i in range(1, len(param)):
        string = param[i]
        if string[-3:] != "ism":
            print(string + "ism")

else:
    print("None")