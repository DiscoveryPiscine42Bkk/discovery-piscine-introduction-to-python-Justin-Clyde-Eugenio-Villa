#!/usr/bin/env python3

def greetings(name="Noble Stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}")
    
    else:
        print("Error! It was not a name.")

greetings("Alex")
greetings("Will")
greetings()
greetings(42)