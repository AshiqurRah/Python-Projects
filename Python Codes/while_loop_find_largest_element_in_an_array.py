
def find_largest_element(arr):
    if len(arr) == 0:
        return None
    
    largest = arr[0]
    i = 1

    while i < len(arr):
        if arr[i] > largest:
            largest = arr[i]
        i += 1
    return largest

arr = [12, 45, 2, 67, 89, 21]
largest_element = find_largest_element(arr)

if largest_element is not None:
    print(f"The largest element in the array is {largest_element}")
else:
    print("The array is empty.")