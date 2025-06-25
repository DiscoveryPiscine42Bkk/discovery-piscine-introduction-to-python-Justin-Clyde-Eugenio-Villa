#!/usr/bin/env python3

def find_the_redheads(head_dict):
    return list(filter(lambda name: head_dict[name] == "red", head_dict.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))