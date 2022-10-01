def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''

    # insert code here
    #error handling
    if type(arr) != list:
        raise TypeError

    for i in range(len(arr)):
        #the first element should be the smallest
        if i == 0:
            minVal = arr[i]
            minIndex = i;
        #if the current element is smaller than the current min, then update the min
        elif arr[i] < minVal:
            minVal = arr[i]
            minIndex = i;
    
    return minIndex
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
    #error handling
    if type(string) != str:
        raise TypeError

    x = []
    #iterate through the string backwards and add each character to the array
    for i in range(len(string)):
        x.append(string[len(string) - 1 - i])
    
    return x
    pass