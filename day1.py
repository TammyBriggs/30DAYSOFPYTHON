def simple_calculator():

    print("a: Addition")
    print("s: Subtraction")
    print("d: Division")
    print("m: Multiplication")
    print("i: Indices")
    print("sqr: Square Root")
    operation = input("What type of calculation do you want to carry out? ")

    if operation == "sqr":
        number_three = int(input("Enter a Number: "))
        print(number_three ** 0.5)

    else:
        number_one = int(input("Enter Number One: "))
        number_two = int(input("Enter Number Two: "))
        if operation == "a":
            print(number_one + number_two)
        elif operation == "s":
            print(number_one - number_two)
        elif operation == "d":
            print(number_one // number_two)
        elif operation == "m":
            print(number_one * number_two)
        elif operation == "i":
            print(number_one ** number_two)
        else:
            print("Incorrect Input, try again")

simple_calculator()

#Deletion
# def deletion(list):
#     list = [11, 2, 33, 14, 5]
#     list.remove(list[-1])
#     print(list)

# deletion(list)