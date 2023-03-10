#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return (0)
    elif not isinstance(roman_string, str):
        return (0)
    else:
        roman_to_int = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
                }
        result = 0
        s = roman_string

        for i in range(len(s)):
            if i > 0 and roman_to_int[s[i]] > roman_to_int[s[i - 1]]:
                result += roman_to_int[s[i]] - (2 * roman_to_int[s[i - 1]])
            else:
                result += roman_to_int[s[i]]
        return result
