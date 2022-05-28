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

    try:
        int(n)
    except:
        raise TypeError
    if n < 1:
        raise TypeError
    if n in [1, 2]:
        return 1

    else:
        return (fibonacci_term(n-1) + fibonacci_term(n-2))
    pass
