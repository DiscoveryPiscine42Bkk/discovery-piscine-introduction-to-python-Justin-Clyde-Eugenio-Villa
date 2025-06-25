#!/usr/bin/env python3

def average(score_dict):
    if not(score_dict):
        return 0
    return sum(score_dict.values())/len(score_dict)

class_3B = {
"marine": 20,
"jean": 11,
"coline": 7,
"luc": 9
}

class_3C = {
"quentin": 13,
"julie": 18,
"marc": 9,
"stephanie": 12
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")