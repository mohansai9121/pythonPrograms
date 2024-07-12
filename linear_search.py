# searching an element using linear search
elements = list(map(str, input("Enter some elements:").split()))
search_element = input("Enter the element to search:")


def linear_search(arr, ele):
    position = -1
    for i in range(len(arr)):
        if ele == arr[i]:
            position = i+1
            break
        else:
            continue
    return position


n = linear_search(elements, search_element)
if n != -1:
    print(f"{search_element} found at position {n} in the list of elements")
else:
    print(f'{search_element} not found in the given list of elements')
