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

    if(n<=0): # raises error for non-positive integers
      raise TypeError

    else:
      if(n == 1 or n == 2):
        return 1

      one = 1
      two = 1

      while(n > 2): #continually add two consecutive terms until n is reached
        temp = one + two
        one = two
        two = temp
        n = n - 1
      return two
    pass
