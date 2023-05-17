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

    #Edge Cases
    
    min = float('inf') #positive infinity
    indexVal = 0
    for i in range(len(arr)):  #Find lowest number
        if arr[i] < min:
            min = arr[i]
    
    return arr.index(min) #returns first index of lowest number



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
    reversed_arr = []
    for i in range(len(s) - 1, -1, -1):
        reversed_arr += s[i]
    return reversed_arr



def most_freq_element(arr: list[int]) -> int:
    """
    Find the value that appears the most frequently in the array.
    If there are multiple, return the value that appears first in the array.
    The array will always have at least 1 element.
    eg. [1, 33, 1, -2, 33] => 33
    eg. [1, 2, 3, 4] => 1
    eg. [3, 5, 1, 5, 3] => 3

    @param array of integers
    @returns integer value that appears the most frequently in the array
    """

    # insert code here
    count = {}

    #store how many of each number appears in a dictionary
    for i in range(len(arr)):
        if arr[i] in count:
            count[arr[i]] += 1
        else:
            count[arr[i]] = 1
        
        max = 0
        maxList = []
        for key in count:
            if count[key] > max:
                max = count[key]
                maxList.append(key)

        return maxList[0]
