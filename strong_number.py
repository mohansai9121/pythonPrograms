import math as m
# To find the number is Strong number or not
n = int(input("Enter a positive number:"))
n = str(n)
sum_of_digits = 0
for i in n:
    sum_of_digits += m.factorial(int(i))
print(f"Sum of factorial of digits in {n}:{sum_of_digits}")
if sum_of_digits == int(n):
    print(f"{n} is \'Strong number\'")
else:
    print(f'{n} is not a \'Strong number\'')
