# Sorting numbers using Selection sort
try:
    numbers = list(map(int, input("Enter the numbers to be sorted:").split()))
    n = len(numbers)
    print(f'size of list of numbers:{n}')
    for i in range(n-1):
        min_element_index = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min_element_index]:
                min_element_index = j
        if i != min_element_index:
            numbers[i], numbers[min_element_index] = numbers[min_element_index], numbers[i]
    print(f'Sorted numbers(Selection sort):{numbers}')
except:
    print("Something went wrong or check the input...!")
