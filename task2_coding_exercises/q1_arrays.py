"""
Complete the following functions.
Test cases can be found in the "tests" folder
"""


def find_min_index(arr: list[int]) -> int:
    """
    Find index where minimum value first occurs in array.
    The array will always have at least 1 element.
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0
    eg. [100] => 0

    @param array of integers
    @returns integer index of minimum integer
    """

    # insert code here
    min = arr[0]
    minIndex = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
            minIndex = i
    return minIndex


def reverse_str_arr(s: str) -> list[str]:
    """
    Return array of string characters, but in reverse order.
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    """

    # insert code here
    a = list(s)
    x = []
    for i in range(len(s) - 1, -1, -1):
        x.append(a[i])
    return x
    


def most_freq_element(arr: list[int]) -> int:
    """
    Find the value that appears the most frequently in the array.
    If there are multiple, return the value that appears first in the array.
    The array will always have at least 1 element.
    eg. [1, 33, 1, -2, 33] => 1
    eg. [1, 2, 3, 4] => 1
    eg. [3, 5, 1, 5, 3] => 3

    @param array of integers
    @returns integer value that appears the most frequently in the array
    """

    # insert code here
    x = arr
    x.sort()
    currentVal = 0
    currentCount = 0
    maxCount = 0
    maxVal = 0
    for i in x:
        if (i == currentVal):
            currentCount += 1
        else:
            currentCount = 1
            currentVal = i
        
        if (currentCount > maxCount):
            maxCount = currentCount
            maxVal = currentVal


    return maxVal
