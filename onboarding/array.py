def find_min_index(arr):
    '''
    Find index where minimum value first occurs in array
    eg. [1, 33, 1, -2, 0] => 3
    eg. [0, 0, 0, 0, 0] => 0

    @param array of integers
    @returns integer index of minimum integer
    '''

    # insert code here
    minimum = arr[0]
    index = 0

    for i in range(len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
            index = i

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
    # insert code here

    stack = []
    returned_stack = []
    for letter in string:
        stack.append(letter)

    for i in range(len(string)):
        returned_stack.append(stack.pop())

    return returned_stack

