n = int(input("Enter a number:"))
factors = [1, n]
if n == 1:
    print('Factor of 1 is:1')
elif n > 2:
    for i in range(2, n//2+1):
        if i not in factors:
            if n % i == 0:
                factors.append(i)
                if i*i != n:
                    factors.append(n//i)
    factors.sort()
    print(f'Factors of {n}:{factors}')
else:
    print("Enter a positive number.")
