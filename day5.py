# 1. Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com' Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# 2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Sample String : 'w3resource' Expected Result : 'w3ce' Sample String : 'w3' Expected Result : 'w3w3' Sample String : ' w' Expected Result : Empty String
# 3. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'

def character_frequency_counter(string):
    character_frequency = {}
    for char in string:
        character_frequency[char] = character_frequency.get(char, 0) + 1
    print(character_frequency)

def string_manipulation(string):
    if len(string) < 2:
        print("")
    else:
        print(string[:2] + string[-2:])

def adding_suffixes(string):
    if len(string) < 3:
        print(string)
    elif string[-3:] == "ing":
        print(string + "ly")
    else:
        print(string + "ing")
    
    
