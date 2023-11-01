
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 

        if arr[mid] == target:  
            return mid
        elif arr[mid] < target:  
            left = mid + 1
        else: 
            right = mid - 1

    return -1  


sorted_array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target_element = 11
result = binary_search(sorted_array, target_element)

if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")
