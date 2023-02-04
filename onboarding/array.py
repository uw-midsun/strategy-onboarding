def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    # checking valid input
    if type(arr) != list:
        return None
    for i in arr:
        if type(i) != int:
            return None

    min_val = min(arr)
    index_val = arr.index(min_val)
    return index_val

def reverse_str_arr(string):
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    '''

    # checking valid input
    if type(string) != str:
        return None

    empty_list = []
    rev_string = string[::-1]
    for i in rev_string:
        empty_list.append(i)

    return empty_list