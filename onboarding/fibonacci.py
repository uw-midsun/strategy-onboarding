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
    if n > 0:
      a = 0
      b = 1
      c = 0
      for i in range(n-1):
        print(i)
        c = a + b
        a = b
        b = c
      return c
    else:
      print("Please enter a value greater than 0")
      raise TypeError
