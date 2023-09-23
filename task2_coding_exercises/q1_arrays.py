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
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            index = i
            min = arr[i]
    return index
    pass


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

    list = []
    for i in reversed(range(0, len(s))):
        list.append(s[i])

    return list
    pass


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

    appear = list()
    for i in range(0, len(arr)):
        new = True
        for j in range(0, len(appear)):
            if arr[i] == appear[j][0]:
                appear[j][1] += 1
                new = False
                break
        if new:
            appear.append([arr[i], 1])
    
    max = appear[0][1]
    value = appear[0][0]   
    for i in range(1, len(appear)):
        if appear[i][1] > max:
            max = appear[i][1]
            value = appear[i][0]
            
    return value
    pass
