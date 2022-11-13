def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''

    # insert code here
    smallnum=arr[0]
    ans=0
    for k in arr:
        if k<smallnum:
            smallnum=k
            ans=arr.index(k)    
    return ans


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
    rever= []
    leng=len(string)-1
    while(leng>=0):
        rever.append(string[leng])
        leng-=1
    return rever