from collections import Counter
# Finding HCF for n numbers
n = int(input("Enter how many numbers:"))
nums = list(map(int, input(f"Enter {n} numbers:").split()))


def prime_factorization(number):
    prime = 2
    facts = []
    while number >= prime * prime:
        if number % prime == 0:
            number //= prime
            facts.append(prime)
        else:
            prime += 1
    if number > 1:
        facts.append(number)
    facts = Counter(facts)
    return facts


def factors(number):
    facts = [1]
    for i in range(2, number+1):
        if number % i == 0 and i not in facts:
            facts.append(i)
    print(f"factors of {number}:{facts}")
    return facts


all_factors = []
for i in nums:
    all_factors.append(factors(i))
# print(f"All factors for each input number:{all_factors}")
common_factors = [1]
for i in all_factors[0]:
    matching = 1
    for j in range(1, len(all_factors)):
        if i not in all_factors[j]:
            break
        else:
            matching += 1
    if matching == len(all_factors):
        common_factors.append(i)
# print(f"Common factors:{common_factors}")
hcf = max(common_factors)
print(f"Highest Common Factor, HCF({nums}):{hcf}")

# LCM of the given input numbers using prime factorization
prime_factors = []
for i in nums:
    prime_factors.append(prime_factorization(i))
print(f'Prime Factors:{prime_factors}')
prime_keys1 = []
for i in prime_factors:
    prime_keys1.append(list(i.keys()))
prime_keys = []
for i in prime_keys1:
    for j in i:
        prime_keys.append(j)
prime_keys = list(set(prime_keys))
print(f'All prime factors for the input numbers are:{prime_keys}')
highest_power_primes = {}
for i in prime_keys:
    power = 0
    for j in prime_factors:
        if power < j[i]:
            power = j[i]
    highest_power_primes[i] = power
print(f'Primes with highest power got using prime factorization:{highest_power_primes}')
lcm = 1
for i in range(len(prime_keys)):
    lcm *= pow(prime_keys[i], highest_power_primes[prime_keys[i]])
print(f'Least Common Multiple, LCM({nums}):{lcm}')
