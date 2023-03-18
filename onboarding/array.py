def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''

    # insert code here
    if (type(arr) != list):
        raise TypeError("Only arrays/lists are allowed")
    for i in range(len(arr)):
        if (type(arr[i]) != int):
            raise TypeError("Only integers are allowed in the array")
    if (arr == []):
        raise TypeError("Array cannot be empty")
    retval = 0
    for i in range(len(arr)):
        if (arr[i] < arr[retval]):
            retval = i
    return retval



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
    if (type(string) != str):
        raise TypeError("Only strings are allowed")
    return list(string)[::-1]
