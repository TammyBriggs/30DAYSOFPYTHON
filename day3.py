# Fibonacci: Write a program that prompts the user to enter a positive integer n, 
# and then prints the first n Fibonacci numbers. The Fibonacci sequence starts with 0 and 1, 
# and each subsequent number is the sum of the two preceding numbers.

def fibonacci(n):
    fibonacci_sequence = [0, 1] 

    for i in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2])

    return fibonacci_sequence

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input. Please enter a positive integer.")
else:
    sequence = fibonacci(n)
    print("The first", n, "Fibonacci numbers are:")
    for number in sequence:
        print(number)