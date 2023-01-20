def find_min_index(arr):
    minVal = min(arr)
    for i in range (0, len(arr)):
        if arr[i] == minVal:
            return i
    return -1

def reverse_str_arr(string):
    arr = list(string)
    arr = arr[::-1]
    return arr