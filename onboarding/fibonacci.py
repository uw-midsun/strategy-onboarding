import pytest
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

    # checking valid inputs
    if type(n) != int or n < 1:
      raise(TypeError)
    
    val1 = 1
    val2 = 1

    if n == 1:
      return val1
    elif n == 2:
      return val2
    else:
      x_n = fibonacci_term(n-1) + fibonacci_term(n-2)
      return x_n