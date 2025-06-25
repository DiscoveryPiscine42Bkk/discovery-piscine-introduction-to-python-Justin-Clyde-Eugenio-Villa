#!/usr/bin/env python3

import sys

param = sys.argv
param_count = len(sys.argv) - 1
new_arr = []

if param_count == 2:
    try:
        start = int(param[1])
        end = int(param[2])

    
        if start <= end:
            for i in range(start, end+1):
                new_arr.append(i)

            print(new_arr)

        else:
            for i in range(start, end-1, -1):
                new_arr.append(i)

            print(new_arr)

    except ValueError:
        print("Error: both parameters must be integers.")

else:
    print("None")