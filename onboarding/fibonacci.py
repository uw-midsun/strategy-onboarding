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
    first = 1
    second = 1

    # first, second terms need to return earlier
    if n == 1 or n == 2:
      return 1
    # type checks
    if n < 1 or type(n) != int:
      raise TypeError

    for _ in range(n - 2):
      result_sum = first + second
      first = second
      second = result_sum

    return second
