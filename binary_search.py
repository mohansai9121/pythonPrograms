# Searching an element using Binary search
numbers = list(map(int, input("Enter list of numbers:").split()))
numbers.sort()
print(f'Sorted numbers:{numbers}')
search_for = int(input("Enter the searching number:"))


def binary_search(nums, lower_index, higher_index):
    low = lower_index
    high = higher_index
    while low <= high:
        mid = low + high // 2
        if nums[mid] == search_for:
            return mid
        elif search_for < nums[mid]:
            high = mid-1
        else:
            low = mid+1
    return -1


index = binary_search(numbers, 0, len(numbers)-1)
if index != -1:
    print(f'{search_for} found in the given numbers')
else:
    print(f'{search_for} not found in the numbers')
