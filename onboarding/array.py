def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    
    if arr == [] or type(arr) != list:
        raise TypeError
    
    min = arr[0]
    index = 0

    for count, value in enumerate(arr) :
        if value < min :
            min = value
            index = count
    return index

def reverse_str_arr(string):
    
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    '''
    
    if type(string) != str :
        raise TypeError
    elif string == '' :
        raise ValueError

    return ([string[i] for i in range(-1, -(len(string) + 1), -1)])   
