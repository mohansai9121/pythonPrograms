n = input("Enter a number:")
length = len(n)
try:
    num = int(n)
    """Using for loop"""
    n1 = 0
    for i in range(length):
        temp = num % 10
        n1 += pow(temp, length)
        num = num // 10
    print("using for loop,", end='')
    if n1 == int(n):
        print(f'{n} is Armstrong number')
    else:
        print(f'{n} is not an Armstrong number')
    """Using while loop"""
    n1 = 0
    num = int(n)
    while num > 0:
        n1 += pow(num % 10, length)
        num = num // 10
    print("Using while loop,", end="")
    if n1 == int(n):
        print(f'{n} is Armstrong number')
    else:
        print(f'{n} is not an Armstrong number')
except:
    print("Entered wrong input")
