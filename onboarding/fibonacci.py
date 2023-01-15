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
    if n < 1: 
      raise TypeError
    elif n == 1 or n == 2: # First/Second values in the Fibonacci sequence
      return 1
    else:
      tmp_term = 0 # Considers third Fibonacci values and onwards
      term1 = 1
      term2 = 1
      for i in range(2, n):
        tmp_term = term1
        term1 = term2
        term2 += tmp_term
      return term2
    pass
