#!/usr/bin/env python3

def array_of_names(name_dict):
    full_names = []
    for first_name, last_name in name_dict.items():
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        full_names.append(full_name)
    return full_names

persons = {
    "jean": "val",
    "grace": "hop",
    "xavier": "niel",
    "fifi": "brin"
}

print(array_of_names(persons))
