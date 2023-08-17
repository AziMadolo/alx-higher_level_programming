def calculate_subtraction(nums):
    subtraction_value = 0
    max_num = max(nums)

    for num in nums:
        if max_num > num:
            subtraction_value += num

    return (max_num - subtraction_value)

def roman_to_int(roman_str):
    if not roman_str:
        return 0

    if not isinstance(roman_str, str):
        return 0

    rom_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numeral_keys = list(rom_numerals.keys())

    num_value = 0
    last_value = 0
    num_list = [0]

    for char in roman_str:
        for numeral in numeral_keys:
            if numeral == char:
                if rom_numerals.get(char) <= last_value:
                    num_value += calculate_subtraction(num_list)
                    num_list = [rom_numerals.get(char)]
                else:
                    num_list.append(rom_numerals.get(char))

                last_value = rom_numerals.get(char)

    num_value += calculate_subtraction(num_list)
    return num_value

if __name__ == "__main__":
    roman_number = "X"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "VII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "IX"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "LXXXVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))

    roman_number = "DCCVII"
    print("{} = {}".format(roman_number, roman_to_int(roman_number)))
