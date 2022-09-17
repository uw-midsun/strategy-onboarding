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
    if not isinstance(n, int) or n <= 0:
      raise TypeError
    first = 1
    second =1
    while n >= 3:
      temp = first + second
      first = second
      second = temp
      n -= 1
    return second
    pass
