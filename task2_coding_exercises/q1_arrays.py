"""
Complete the following functions.
Test cases can be found in the "tests" folder
"""
import numpy as np

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

    return np.argmin(arr)



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

    arr1 = []
    for i in s:
        arr1.append(i)
    arr2 = arr1[::-1]
    return arr2


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


    max_count = 0
    most_frequent = 0
    for i in range(0,len(arr)):
        counter = 0
        for j in range(0,len(arr)):
            if arr[i] == arr[j]:
                counter+=1
        if counter > max_count:
            max_count = counter
            most_frequent = arr[i]
    return most_frequent

    pass
