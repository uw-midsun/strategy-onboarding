def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    if len(arr) == 0:
        return -1
    else:
        minIndex = 0
        minVal = arr[0]
        for x in range(1, len(arr)):
            if(arr[x] < minVal):
                minVal = arr[x]
                minIndex = x
            
        return minIndex


def reverse_str_arr(string):
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']

    @param string
    @returns array of characters
    '''

    arr = []
    for x in range(len(string) - 1, -1, -1):
        arr.append(string[x])
    return arr