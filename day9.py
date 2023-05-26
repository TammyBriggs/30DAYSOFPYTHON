# 1. Write a Python program to check whether an element exists within a tuple.
# 2. Write a Python program to convert a list to a tuple.

#1
def check_element_in_tuple(element, tuple_data):
    return element in tuple_data

tuple_data = (10, 20, 30, 40, 50)
element = 15

if check_element_in_tuple(element, tuple_data):
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")

#2
def convert_list_to_tuple(list_data):
    print(tuple(list_data))

# convert_list_to_tuple([1,2,3,4,5,6])