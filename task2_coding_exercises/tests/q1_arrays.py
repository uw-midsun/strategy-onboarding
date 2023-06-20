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
    min_value = arr[0]
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i

    print(min_index)
    return min_index

find_min_index([100])

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
    s_length = len(s)
    arr = [''] * s_length
    count = -1 

    for i in s:
        arr[count] = i  # start the index from the last character in the array
        count -= 1  
    
    print(arr)

    return arr

reverse_str_arr("")    


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
    number_dict = {} 

    for i in arr:
        
        if number_dict.get(i) is None:
            number_dict[i] = 1
        else:
            number_dict[i] += 1
    
    most_freq_value = 0
    element = 0
    for key in number_dict: 
        if (number_dict.get(key) > most_freq_value):
            most_freq_value = number_dict.get(key)
            element = key 

    print (element)
    return element    

most_freq_element([1, 2, 3, 4])