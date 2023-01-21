def fibonacci_term(n):

    '''
    Finds nth term of the Fibonacci sequence from:
        Term | value
        ------------
          1  |   1
          2  |   1
          3  |   2
          4  |   3
          5  |   5
         ... |  ...

    @params n: integer
    @returns integer, nth term of the Fibonacci sequence
    '''
    if n <= 0:
        raise TypeError
    # insert code here
    first = 1
    second = 1
    result = 0

    if (n == 1 or n == 2):
        return 1

    for i in range(2, n):
        result = first + second
        first = second
        second = result

    return result
