#!/usr/bin/env python3

org_arr = [2, 3, 8, 7, 42, -10, 2]
new_arr = []

for i in org_arr:
    if i>5:
        new_arr.append(i + 2)

print(f"Original Array {org_arr}")
print(f"New array: {new_arr}")