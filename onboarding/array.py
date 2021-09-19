
def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    if (len(arr) == 0):
        raise IndexError

    min = float('inf')
    index = 0
    min_index = 0

    for item in arr:
        if item < min:
            min_index = index
            min = item
        index = index + 1
    
    return min_index
        
    

def reverse_str_arr(string):
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    '''
    if (len(string) == 0):
        raise ValueError

    reverse = list(string)
    reverse.reverse()


    return reverse

