def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    

    lowestIndex = 0
    lowestNum = arr[0]

    for i, num in enumerate(arr):
        if num < lowestNum:
            lowestNum = num
            lowestIndex = i


    return lowestIndex
    # insert code here
    pass


def reverse_str_arr(string):
    '''
    Return array of string characters, but in reverse order
    eg. "abc" => ['c', 'b', 'a']
    eg. "abba" => ['a', 'b', 'b', 'a']
    eg. "!!-.2" => ['2', '.', '-', '!', '!']
s
    @param string
    @returns array of characters
    '''
    
    ansArr = []
    
    for i, character in enumerate(string):
        ansArr.append(string[len(string)-i-1])
    
    return ansArr
    pass