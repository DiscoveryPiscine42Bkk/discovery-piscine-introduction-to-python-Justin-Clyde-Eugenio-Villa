#!/usr/bin/env python3

i = 0

while i < 11:
    j = 0
    print("Table de ", i, ": ", end=" ")
    while j < 11:
        ans = i*j
        print(ans, end=" ")
        j += 1
    print()
    i += 1