#!/usr/bin/env python3

org_arr = [2, 3, 8, 7, 42, 8, -10, 2, 7]
new_set = set()

for i in org_arr:
    if i>5:
        new_set.add(i + 2)

print(f"Original Array {org_arr}")
print(f"New Set: {new_set}")