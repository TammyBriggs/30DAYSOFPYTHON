# 1. Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels from the trolls’ comments, neutralizing the threat. Your task is to write a function that takes a string argument and returns a new string with all vowels removed. For example, the string “Hello World!” would become “Hll Wrld”. Note: For this problem, ‘y’ is NOT considered a vowel.
# 2. Write a Python program to match if two words from a list of words start with the letter 'P'.
# 3. Write a Python program to remove the parenthesis area in a string. Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"] Expected Output: example w3resource github stackoverflow

#1
def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    print(''.join(char for char in text if char not in vowels))

#2
def check_words_start_with_P(word_list):
    # Initialize a counter to keep track of words starting with 'P'
    count = 0

    # Iterate over the words in the list
    for word in word_list:
        # Check if the word starts with 'P'
        if word.startswith('P'):
            count += 1

            if count == 2:
                print("Two words start with 'P' in the list.")

    print("There are no two words starting with 'P' in the list.")

#3
import re

def remove_parenthesis_area():
    strings = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
    for string in strings:
        print(re.sub(r" ?\([^)]+\)", "", string))

remove_parenthesis_area()
        