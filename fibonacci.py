# Program to print n fibonacci numbers
n = int(input("Enter a number:"))
fibonacci = [0, 1]
if n > 0:
    if n == 1:
        print('1st fibonacci number is:[0]')
    elif n == 2:
        print(f'2 fibonacci numbers are:{fibonacci}')
    else:
        for i in range(n-2):
            length = len(fibonacci)-1
            fibonacci.append(fibonacci[length]+fibonacci[length-1])
        print(f'{n} Fibonacci numbers are:{fibonacci}')
        print(f'{n}th Fibonacci number is:{fibonacci[n-1]}')
else:
    print("Enter a positive number.")
