# To find the number is Automorphic number or not
n = int(input("Enter a number:"))
length = len(str(n))
square_of_n = n*n
print(f"Square of the number {n} is:{square_of_n}")
if square_of_n % 10**length == n:
    print(f"{n} is \'Automorphic Number\'")
else:
    print(f"{n} is not an Automorphic Number")
