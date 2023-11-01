def is_sorted_ascending(arr):
    if not arr:
        return True
    
    index = 0
    while index < len(arr) - 1:
        if arr[index] > arr[index + 1]:
            return False
        index += 1

    return True

my_list = [1, 2, 3, 4, 5]
if is_sorted_ascending(my_list):
    print("The list is sorted in ascending order.")
else:
    print("The list is not sorted in ascending order.")