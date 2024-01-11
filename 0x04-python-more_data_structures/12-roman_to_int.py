#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    int_value = 0
    roman_data = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in roman_data.keys():
            return 0
        elif roman_data[i] >= roman_data[j]:
            int_value += roman_data[i]
        else:
            int_value -= roman_data[i]
    int_value += roman_data[roman_string[-1]]
    return int_value
