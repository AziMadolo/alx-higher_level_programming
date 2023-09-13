#!/usr/bin/python3
"""Defines a function to convert a class instance to a dictionary."""

def class_to_json(obj):
    """Convert a class instance to a dictionary representation."""
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return {}
