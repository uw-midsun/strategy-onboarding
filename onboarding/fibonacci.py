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

    # insert code here
    if type(n) != int or n <= 0:
        raise TypeError
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a
