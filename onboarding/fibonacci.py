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
    if n <= 0:
      raise TypeError("Non-postive input")
    if n == 1 or n == 2:
      return 1
    
    a = 1
    b = 1
    for i in range(3, n+1):
      a, b = b, a
      b = a + b

    return b
