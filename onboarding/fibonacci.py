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

    # in case of negative number
    n = abs(n)

    if n <= 2:
        return 1

    n1 = 1
    n2 = 1
    
    for i in range(n-2):
        n_term = n1 + n2
        n1 = n2
        n2 = n_term

    return n_term
