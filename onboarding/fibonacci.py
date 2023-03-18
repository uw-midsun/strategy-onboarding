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
    if (type(n) != int):
      raise TypeError("Only Integers are allowed")
    elif (n <= 0):
      raise TypeError("Only Positive Integers allowed")
    a = 1
    b = 1
    if n == 1:
        return b
    else:
        for _ in range(2, n):
            c = a + b
            a = b
            b = c
        return b
