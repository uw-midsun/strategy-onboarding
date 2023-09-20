"""
Complete the following functions.
Test cases can be found in the "tests" folder
"""

import sys

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
    min = 0

    for i in range(len(arr)):
        if arr[i] < arr[min]:
            min = i

    return min

print(find_min_index([1, 33, 1, -2, 0])) 
print(find_min_index([0, 0, 0, 0, 0])) 
print(find_min_index([100])) 

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
    reversed = []

    for i in range(len(s)):
        reversed.append(s[len(s) - 1 - i])

    return reversed

print(reverse_str_arr("abc"))
print(reverse_str_arr("abba"))
print(reverse_str_arr("!!-.2"))

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
    count = 0
    num = arr[0]

    for i in arr:
        currCount = arr.count(i)
        if currCount > count:
            count = currCount
            num = i

    return num
    
print(most_freq_element([1, 33, 1, -2, 33]))
print(most_freq_element([1, 2, 3, 4]) )
print(most_freq_element([3, 5, 1, 5, 3]))
