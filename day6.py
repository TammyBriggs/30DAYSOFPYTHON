# 4. Write a Python program to remove duplicates from a list.
# 5. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']
# 6. Write a Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False. Sample Data: ([0, 3, 4, 7, 9]) -> False ([3, 5, 7, 13]) -> True ([1, 5, 3]) -> False

def remove_duplicates(lst):
    print(list(set(lst)))

def remove_elements(lst):
    indices_to_remove = [0, 4, 5]
    updated_lst = [item for i, item in enumerate(lst) if i not in indices_to_remove]
    print(updated_lst)

# def prime_number(numbers):
#     if numbers < 2:
#         print(False)