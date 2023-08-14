#!/usr/bin/python3
# 8-multiple_returns.py

def different_returns(input_text):
    """Calculate length and provide first character of a string."""
    if input_text == "":
        return (0, None)
    return (len(input_text), input_text[0])
