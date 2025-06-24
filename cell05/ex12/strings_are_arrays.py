#!/usr/bin/env python3

import sys

param = sys.argv
param_count = len(sys.argv) - 1

if param_count == 1:
    string = param[1]
    result = ""

    for i in string:
        if i == "z":
            result += "z"


    if result:
        print(result)
    else:
        print("None")

else:
    print("None")