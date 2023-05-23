"""
The functions below are incomplete and/or have a bug in them. 
Fix them so that they work with the examples given.
Test cases can be found in the "tests" folder
"""


def adjacent_subtraction(arr: list[int]) -> list[int] | None:
    """
    Returns a list of numbers where result[i] is the value of arr[i+1] - arr[i].
    The returned array will have 1 less element than arr.
    Return None if arr is empty.
    eg. [1, 6, 3, 2, 8] => [5, -3, -1, 6]
    eg. [1, 2, 3, 4] => [1, 1, 1]
    eg. [1] => []
    eg. [] => None

    @param array of integers
    @returns array of integers or None
    """

    if len(arr) == 0:
        return None

    results = []
    for i in range(len(arr)):
        if i < len(arr) - 1:
            first = arr[i]
            second = arr[i + 1]
            results.append(second - first)

    return results


def str_math(arr: list[str]) -> int | float | None:
    """
    Add all the number strings in arr together.
    eg. ["1", "6", "3", "2", "8"] => 20
    eg. ["1", "b", "3", "-2", []] => 2
    eg. ["1", "b", "3.5", "-12"] => -7.5
    eg. ["hi"] => None
    eg. [] => None

    @param array of strings
    @returns an int, float, or None
    """
    total = 0
    if not arr:
        return None
    for s in arr:
        if isinstance(s, str):
            if not s.isalpha():
                if total == None:
                    total = float(s)
                else:
                    total = total + float(s)

    return total
