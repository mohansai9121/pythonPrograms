# To find the number is Harshad Number or not
n = input("Enter a number:")
sum_of_digits = 0
for i in n:
    sum_of_digits += int(i)
print(f'SUm of digits in the number is:{sum_of_digits}')
if int(n) % sum_of_digits == 0:
    print(f'{n} is \'Harshad Number\'')
else:
    print(f"{n} is not a \'Harshad Number\'")
