#!/usr/bin/env python3

import sys

param = sys.argv

# user_input = input("What was the parameter?: ")

if len(param) - 1 == 1:
    user_input = input("What was the parameter?: ")
    if param[1] == user_input:
        print("Good Job!")
    else:
        print("Nope, sorry...")
else:
    print("None")