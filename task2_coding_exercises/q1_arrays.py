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
    minimum_value = arr[0]
    minimum_index = 0
    for x in range(len(arr)):
        if (arr[x] < minimum_value) : 
            minimum_value = arr[x]
            minimum_index = x
    
    return minimum_index

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
    input_array = list(s)
    input_array.reverse()
    return input_array

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
    freq_dict = {}
    for i in arr:
        if i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
        else:
            freq_dict[i] = 1
    
    freq = 0
    num = 0
    for i in arr:
        if freq_dict[i] > freq:
            num = i
            freq = freq_dict[i]

    return num
    pass
