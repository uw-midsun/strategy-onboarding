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
    lookup = {}

    if n < 1:
        raise TypeError("n must be a positive integer")

    def compute_recursive(n):
        '''
        Recursive helper function
        '''

        if (lookup.get(n)):
            return lookup[n]

        if (n <= 2):
            return 1

        value = compute_recursive(n - 1) + compute_recursive(n - 2)
        lookup[n] = value

        return value

    return compute_recursive(n)
