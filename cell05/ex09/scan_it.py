#!/usr/bin/env python3

import sys
import re

if len(sys.argv) - 1 == 2:
    match = re.findall(sys.argv[1], sys.argv[2])
    if len(match) > 0:
        print(len(match))
    else:
        print("None")

else:
    print("None")