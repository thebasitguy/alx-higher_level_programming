#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    mapping_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_values = [mapping_data[x] for x in roman_string] + [0]
    result = 0

    for i in range(len(int_values) - 1):
        if int_values[i] >= int_values[i+1]:
            result += int_values[i]
        else:
            result -= int_values[i]

    return result
