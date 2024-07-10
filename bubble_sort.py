# Sorting the elements using Bubble sort algorithm
try:
    numbers = list(map(int, input("Enter numbers to be sorted(space separated):").split()))
    n = len(numbers)
    print(f"size of list:{n}")
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j+1] < numbers[j]:
                numbers[j+1], numbers[j] = numbers[j], numbers[j+1]
    print(f'Bubble Sort(ascending order):{numbers}')
except:
    print("Input wrong...!")
