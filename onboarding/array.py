def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    if isinstance(arr, str):
        raise TypeError
    try:
        len(arr)
    except:
        raise TypeError
    min_val = None
    min_index = None
    for index, val in enumerate(arr):
        if index == 0:
            min_val = val
            min_index = index
        elif val < min_val:
            min_val = val
            min_index = index
    return min_index
    pass


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
    print(type(string))
    if not isinstance(string, str):
        raise TypeError

    if len(string) != 0:
        return list(string)[::-1]
    pass
