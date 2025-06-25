#!/usr/bin/env python3

import sys
param = sys.argv

def downcase_all(p):
    result = []

    for element in p[1:]:
        result.append(element.lower())

    return result


result = downcase_all(param)

if result:
    for word in result:
        print(word)
else:
    print("None")
