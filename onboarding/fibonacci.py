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

    if (n < 1):
        raise TypeError()
    
    current = 1
    prev = 1

    for i in range (2, n):
        temp = current + prev
        prev = current
        current = temp

    return current
