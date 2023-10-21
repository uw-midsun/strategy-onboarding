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
    index = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[index]:
            index = i

    return index 
    
    

def reverse_str_arr(s: str) -> list[str]:
    """
    Return array of string characters, but in reverse order.
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    """

    result = []

    for i in range (len(s)-1, -1, -1): 
        result.append(s[i])
    
    return result
    


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

    element_max = 0
    max_count = 0
    count = 0

    for i in range (len(arr)):
        for j in range (i, len(arr)): 
            if arr[i] == arr[j]: 
                count += 1

        if count > max_count:
            element_max = arr[i]
            max_count = count
        
        count = 0

    return element_max
    pass