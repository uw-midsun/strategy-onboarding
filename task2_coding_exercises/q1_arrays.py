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

    lowest_index = 0
    # range starts at one as lowest_index is zero
    for i in range(1, len(arr)):
        if (arr[i] < arr[lowest_index]):
            lowest_index = i
    return lowest_index


def reverse_str_arr(s: str) -> list[str]:
    """
    Return array of string characters, but in reverse order.
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    """

    # reverse the contents of the string
    reverse_string = s[::-1]
    reverse_list = []

    for letter_index in range(0, len(reverse_string)):
        reverse_list.append(reverse_string[letter_index])
    return reverse_list


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

    # new dictionary, corresponding repetitions to the values
    match = {}
    for val in arr:
        if val in match:
            match[val] += 1
        else:
            match[val] = 1
    
    # compare repetitions for each value
    val = arr[0]
    rep_val = match[val]
    for values in arr:
        if match[values] > rep_val:
            rep_val = match[values]
            val = values
            
    return val
