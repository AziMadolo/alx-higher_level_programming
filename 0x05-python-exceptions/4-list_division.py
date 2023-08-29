#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(0, list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except (ZeroDivisionError, TypeError, IndexError):
            div = 0
        finally:
            new_list.append(div)
    return new_list

if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
