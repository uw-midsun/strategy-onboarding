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

    Parameters:
    arr (list of int): The input list of integers.

    Returns:
    list of int or None: The list of differences or None if arr is empty.
    """

    if not arr:
        return None
    
    if len(arr) == 1:
        return [arr[0]]
    
    results = []

    for i in range(len(arr) - 1):
        first = arr[i]
        second = arr[i + 1]
        results.append(second - first)

    return results


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
    if not arr:
        return None
    
    total = 0
    for s in arr:
        try:
            newInt = int(s)
            total += newInt
        except:
            try:
                newFloat = float(s)
                total += newFloat
            except:
                pass

    return total
