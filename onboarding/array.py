def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''

    # insert code here
    if len(arr) == 0:
        raise TypeError
    else:
        min_index = 0
        index = 0
        min_value = arr[0]

        for i in arr:
            if i < min_value:
                min_value = i
                min_index = index
            else:
                index += 1
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
    arr = []
    for i in range(len(string) -1, -1, -1):
        arr.append(string[i])
    return arr
    pass