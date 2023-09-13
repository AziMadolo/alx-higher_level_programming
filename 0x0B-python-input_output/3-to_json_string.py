#!/usr/bin/python3
"""Defines a function to convert objects to JSON strings."""
import json


def to_json_string(my_obj):
    """Convert an object to a JSON string."""
    return json.dumps(my_obj)
