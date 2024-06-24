# Program to print n lines of pascal triangle
import math
n = int(input("Enter number of rows for Pascal's Triangle:"))
for i in range(n):
    for j in range(n-i):
        print("\t", end='')
    for j in range(i+1):
        fact = math.factorial(i)//(math.factorial(j)*math.factorial(i-j))
        print(fact, end='\t\t')
    print()
