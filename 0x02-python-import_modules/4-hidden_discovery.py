#!/usr/bin/python3

if name == "main":
"""Display all the names that are present in the hidden_4 module."""
import hidden_4 as h

name_list = dir(h)
for n in name_list:
    if n[:2] != "__":
        print(n)
