#!/usr/bin/env python3

import sys
param = sys.argv
param_count = len(sys.argv) - 1

def shrink(pm):

    return pm[:8]

def enlarge(pm):
    while len(pm) < 8:
        pm += "z"

    return pm

if param_count > 0:
    for element in param:
        if len(element) > 8:
            result = shrink(element)

        else:
            result = enlarge(element)

        print(result)
else:
    print("None")


