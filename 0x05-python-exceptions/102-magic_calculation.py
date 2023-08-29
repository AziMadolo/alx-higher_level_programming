#!/usr/bin/python3

def custom_calculation(x, y):
    outcome = 0
    for idx in range(1, 3):
        try:
            if idx > x:
                raise Exception('Exceeded limit')
            else:
                outcome += x ** y / idx
        except:
            outcome = y + x
            break
    return outcome
