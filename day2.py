def complex_calculator():

    print("a: Addition")
    print("s: Subtraction")
    print("d: Division")
    print("m: Multiplication")
    print("i: Indices")
    print("sqr: Square Root")
    print("e: Exit")
    operation = input("What type of calculation do you want to carry out? ")

    if operation == "sqr":
        number_three = int(input("Enter a Number: "))
        print(number_three ** 0.5)

    elif operation == "e":
        print("Successfully Exited")

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

complex_calculator()