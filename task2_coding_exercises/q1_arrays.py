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
    min_index = 0
    min_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < min_num:
            min_index = i
            min_num = arr[i]
    return min_index


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
    stack = []
    ans = []
    for word in s:
        stack.append(word)
    while stack:
        letter = stack.pop()
        ans.append(letter)
    return ans


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
    freq = {}
    maxx = 0
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    # if freq[num] > maxx:
    #     maxx = freq[num]
    #     highest_freq = num
    # elif freq[num] == maxx and arr.index(num) < arr.index(highest_freq):
    #     highest_freq = num
    # return highest_freq

    maxx = 0
    for num in freq.keys():
        if freq[num] > maxx:
            highest_freq = num
            maxx = freq[num]
    return highest_freq
