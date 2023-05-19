# 1.write a function in python that takes a list of numbers and returns the sum of the given numbers. 
# 2. write a function in python that takes a list of numbers and returns the second-largest item in the list of the given numbers. 
# 3. write a function in python that takes 3 parameters: name, age, and occupation and prints this sentence as output: "My name is {name}, I am {age} years old and I work as a {occupation}". 

def list_sum(numbers):
    total = sum(numbers)
    print(total)

def second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    
    sorted_numbers = sorted(numbers, reverse=True)
    print(sorted_numbers[1])

def about(name, age, occupation):
    print(f"My name is {name}, I am {age} years old, and I work as a {occupation}")
