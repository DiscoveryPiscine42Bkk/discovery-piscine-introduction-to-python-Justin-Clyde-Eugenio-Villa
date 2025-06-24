#!/usr/bin/env python3

import sys

param_count = len(sys.argv) - 1

if param_count > 1:
    i = param_count
    while i > 0:
        print(sys.argv[i])
        i -= 1
else:
    print("None")