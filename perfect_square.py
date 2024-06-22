# To find the number is Perfect Square or not
n = int(input("Enter a number:"))
perfect_square = False
for i in range(1, n+1):
    if i*i == n:
        perfect_square = True
        print(f'Square root of {n} is:{i}')
        break
    else:
        continue
if perfect_square:
    print(f"So, {n} is a \'Perfect Square\'")
else:
    print(f"{n} is not a \'Perfect Square\'")
