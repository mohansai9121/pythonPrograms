# To find Factorial of the number
import math

n = int(input("Enter a number:"))


def factorial(num):
    if num < 2:
        return 1
    else:
        return num*factorial(num-1)


if n < 0:
    print(f"Cannot find factorial for {n}")
else:
    """Using for loop"""
    fact = 1
    if n > 1:
        for i in range(2, n+1):
            fact *= i
    print(f'Factorial of {n} using for loop is:{fact}')
    """Using while loop"""
    fact1 = 1
    n1 = n
    if n1 > 1:
        while n1 > 1:
            fact1 *= n1
            n1 -= 1
    print(f'Factorial of {n} using while loop is:{fact1}')
    print(f'Factorial of {n} using recursion is:{factorial(n)}')
    print(f'Factorial of {n} using math module:{math.factorial(n)}')
