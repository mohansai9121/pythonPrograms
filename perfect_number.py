# To find whether the number is perfect number or not
n = int(input("Enter a positive number:"))

def factors(num):
    facts = []
    for i in range(1, n):
        if num % i == 0:
            facts.append((i))
    return facts

proper_factors = factors(n)
print(f"Proper factors are:{proper_factors}")
proper_factors_sum = sum(proper_factors)
if proper_factors_sum == n:
    print(f"{n} is \'Perfect number\'")
else:
    print(f"{n} is not a \'Perfect number\'")