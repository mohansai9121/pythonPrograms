# Program to print prime numbers within the given range of numbers
m = int(input("Enter lower limit:"))
n = int(input("Enter upper limit:"))
primes = []
m1 = m
isPrime = True
if 1 < n > m >= 0:
    if m == 1 or m == 0:
        m1 = 2
    for i in range(m1, n+1):
        for j in range(2, i//2+1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
        isPrime = True
    print(f'Prime numbers between {m} and {n} are:{primes}')
    print(f'Total number of prime numbers between {m} and {n} are:{len(primes)}')
else:
    print('Given wrong Inputs.')
