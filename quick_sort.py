# Sorting the numbers using quick sort
numbers = list(map(int, input("Enter the numbers to be sorted:").split()))


def partition(arr, start_index, end_index):
    start1 = start_index+1
    end1 = end_index
    pivot = arr[start_index]
    while start1 < end1:
        while arr[start1] < pivot:
            start1 += 1
        while arr[end1] > pivot:
            end1 -= 1
        if start1 < end1:
            arr[start1], arr[end1] = arr[end1], arr[start1]
    arr[start_index] = arr[end1]
    arr[end1] = pivot
    return end1


def quick_sort(arr, start_index, end_index):
    if start_index < end_index:
        partition_index = partition(arr, start_index, end_index)
        quick_sort(arr, start_index, partition_index - 1)
        quick_sort(arr, partition_index + 1, end_index)


quick_sort(numbers, 0, len(numbers) - 1)
print(f'Numbers after sorted(quick sort):{numbers}')
