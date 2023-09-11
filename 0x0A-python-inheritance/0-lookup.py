#!/usr/bin/python3
"""Defines a function to look up object attributes."""


def lookup(obj):
    """Return a list of an object's available attributes."""
    return dir(obj)
