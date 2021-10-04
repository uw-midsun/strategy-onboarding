def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''
    if len(arr)==0:
        raise TypeError()

    min = 0

    for i in range(len(arr)):
        if type(arr[i]) != int:
          raise TypeError()
        if arr[i] < min:
            min = i
            print(arr[i])

    return min


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
        raise TypeError()

    arr = []

    for i in string:
        arr.insert(0, i)

    return arr
