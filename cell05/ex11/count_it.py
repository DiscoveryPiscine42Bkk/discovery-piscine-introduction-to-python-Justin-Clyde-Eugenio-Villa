#!/usr/bin/env python3

import sys

param = sys.argv
param_count = len(sys.argv) - 1

print(f"Parameters = {param_count}")

for i in param[1:]:
    length = len(i)
    print(f"{i}: {length}")