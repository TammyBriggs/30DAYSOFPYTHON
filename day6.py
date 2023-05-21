# 1. Write a Python program to combine two dictionary by adding values for common keys. d1 = {'a': 100, 'b': 200, 'c':300} d2 = {'a': 300, 'b': 200, 'd':400} Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
# 2. Write a Python program to create a dictionary from a string. Note: Track the count of the letters from the string. Sample string : 'w3resource' Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
# 3. Write a Python program to sort Counter by value. Sample data : {'Math':81, 'Physics':83, 'Chemistry':87} Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]

#1
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combined_dict = Counter(d1) + Counter(d2)
print(combined_dict)

#2
from collections import Counter

string = 'Flabbergasted'
letter_count = Counter(string)
print(letter_count)

#3
from collections import Counter

data = {'Math': 81, 'Physics': 83, 'Chemistry': 87}
sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(sorted_data)
