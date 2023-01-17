def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    if not isinstance(arr, list):
        raise TypeError()
    if len(arr) == 0:
        return -1
    for el in arr:
        if not isinstance(el, int):
            raise TypeError()
    return arr.index(min(arr))


def reverse_str_arr(string):
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    '''

    # insert code here
    if not isinstance(string, str):
        raise TypeError()

    result = []
    for c in reversed(string):
        result += c
    return result
