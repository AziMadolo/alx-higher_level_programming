#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
import json

def save_to_json_file(my_list, filename):
    """Save a list to a JSON file."""
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_list, file)

def load_from_json_file(filename):
    """Load a list from a JSON file."""
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")

