# Sorting numbers using insertion sort
numbers = list(map(int, input("Enter numbers to be sorted(Space separated):").split()))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


insertion_sort(numbers)
print(f'Numbers after sorting(Insertion sort):{numbers}')
