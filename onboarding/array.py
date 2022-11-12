def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    arr_min = min(arr)

    minimum_list = []

    for n in range(0, len(arr)):
        if arr[n] == arr_min:
             minimum_list.append(n)
    
    print(minimum_list[0])
    return minimum_list[0]




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
    string_list = list(string)
    string_list.reverse()
    print(string_list)
    return string_list

