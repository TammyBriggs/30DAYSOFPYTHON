# 1. Write a Python program to count the number of characters (character frequency) in a string. Sample String : google.com' Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
# 2. Write a Python program to get a string made of the first 2 and last 2 characters of a given string. If the string length is less than 2, return the empty string instead. Sample String : 'w3resource' Expected Result : 'w3ce' Sample String : 'w3' Expected Result : 'w3w3' Sample String : ' w' Expected Result : Empty String
# 3. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged. Sample String : 'abc' Expected Result : 'abcing' Sample String : 'string' Expected Result : 'stringly'
# 4. Write a Python program to remove duplicates from a list.
# 5. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
# 6. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False. Sample Data: ([0, 3, 4, 7, 9]) -> False ([3, 5, 7, 13]) -> True ([1, 5, 3]) -> False

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

def remove_duplicates(lst):
    print(list(set(lst)))

def remove_elements(lst):
    indices_to_remove = [0, 4, 5]
    updated_lst = [item for i, item in enumerate(lst) if i not in indices_to_remove]
    print(updated_lst)

# def prime_number(numbers):
#     if numbers < 2:
#         print(False)
    
    
