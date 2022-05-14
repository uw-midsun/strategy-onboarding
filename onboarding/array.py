from itertools import count


def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    
    if type(arr) != list:
        raise(TypeError)

    # insert code here
    min = arr[0]
    dictionary = {}
    counter = 0
    for i in arr:
        if i < min:
            min = i
        if i not in dictionary:
            dictionary[i] = counter
        counter +=1 
        
    return dictionary[min]

def reverse_str_arr(string):
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    '''
    if type(string) != str:
        raise(TypeError)
    # insert code here
    return list(reversed(list(string)))
    pass