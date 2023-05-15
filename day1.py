#1
def addition_calculator(a, b):
    print(a + b)

addition_calculator(20, 10)

#2
def subtraction_calculator(a, b):
    print(a - b)

subtraction_calculator(20, 10)

#3
def deletion(list):
    list = [11, 2, 33, 14, 5]
    list.remove(list[-1])
    print(list)

deletion(list)

#4
def division_calculator(a, b):
    print(a / b)

division_calculator(20, 10)

#5
def indices_calculator(a, b):
    print(a ** b)

indices_calculator(10, 2)

#6
from math import sqrt

def squareroot_calculator(a):
    print(sqrt(a))

squareroot_calculator(100)