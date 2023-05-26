# 1. Write a Python program to find all the unique combinations of 3 numbers from a given list of numbers, adding up to a target number.
# 2. Write a Python program to return a new set with unique items from both sets by removing duplicates. Given: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} Expected output: {70, 40, 10, 50, 20, 60, 30}
# 3. Update the first set with items that don’t exist in the second set Given two Python sets, write a Python program to update the first set with items that exist only in the first set and not in the second set. Given: set1 = {10, 20, 30} set2 = {20, 40, 50} Expected output: set1 {10, 30}

import itertools

def find_combinations(nums, target):
    result = []
    combinations = itertools.combinations(nums, 3)
    for comb in combinations:
        if sum(comb) == target:
            result.append(comb)
    return result

nums = [1, 2, 3, 4, 5, 6, 7]
target = 12

combinations = find_combinations(nums, target)
print(combinations)

#2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

unique_set = set1.union(set2)
print(unique_set)

#3
set1 = {10, 20, 30}
set2 = {20, 40, 50}

set1.difference_update(set2)
print(set1)