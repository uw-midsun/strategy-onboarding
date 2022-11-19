def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''

    # insert code here
    for i in arr:
        if not type(i) is int:
            raise TypeError
        
    minimum = min(arr)

    return arr.index(minimum)


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

    if not type(string) is str:
            raise TypeError
        
    list_output = list(string)

    return list_output[::-1]



