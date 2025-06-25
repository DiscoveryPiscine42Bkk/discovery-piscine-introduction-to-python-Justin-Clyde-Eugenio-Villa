#!/usr/bin/env python3

def find_the_redheads(head_dict):
    redheads =[]
    for name, hair in head_dict.items():
        if hair == "red":
            redheads.append(name)
    return(redheads)


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}

print(find_the_redheads(dupont_family))