"""
The functions below are incomplete and/or have a bug in them. 
Fix them so that they work with the examples given.
Test cases can be found in the "tests" folder
"""

def adjacent_subtraction(arr: list[int]):
    """
    Returns a list of numbers where result[i] is the value of arr[i+1] - arr[i].
    The returned array will have 1 less element than arr.
    Return None if arr is empty.
    eg. [1, 6, 3, 2, 8] => [5, -3, -1, 6]
    eg. [1, 2, 3, 4] => [1, 1, 1]
    eg. [1] => [1]
    eg. [] => None

    @param array of integers
    @returns array of integers or None
    """
    
    results = []
    
    """if there is only one element in the array, return that element since there is nothing to subtract"""
    if len(arr) == 1:
        results.append( arr[0])
    else:
        """-1 since we cann't subtract the max with anything"""
        for i in range(len(arr) - 1): 
            first = arr[i]
            second = arr[i + 1]
            results.append(second - first)

    return results

print( adjacent_subtraction([1, 6, 3, 2, 8]))
print(adjacent_subtraction([1, 2, 3, 4]))
print(adjacent_subtraction([1]))
print( adjacent_subtraction([]))

def str_math(arr: list[str]):
    """
    Add all the number strings in arr together.
    eg. ["1", "6", "3", "2", "8"] => 20
    eg. ["1", "b", "3", "-2", []] => 2
    eg. ["1", "b", "3.5", "-12"] => -7.5
    eg. ["hi"] => 0
    eg. [] => None

    @param array of strings
    @returns an int, float, or None
    """
    total = 0
    for s in arr:
        try:
            """do not round to an int!"""
            total += float(s)
        except:
            pass

    return total

print(str_math(["1", "6", "3", "2", "8"]))
print(str_math(["1", "b", "3", "-2", []]))
print(str_math(["1", "b", "3.5", "-12"]))
print(str_math(["hi"]))