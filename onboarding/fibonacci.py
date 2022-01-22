from typing import Type

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

    '''
    Value error:
      - Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value
      - the float function can take a string, ie float('5'), it's just that the value 'string' in float('string') is an inappropriate (non-convertible) string

    Type error:
      - Passing arguments of the wrong type (e.g. passing a list when an int is expected) should result in a TypeError
      - so you would get a TypeError if you tried float(['5']) because a list can never be converted into a float.
    '''

    if n < 1 or type(n) != int:
      raise TypeError
    
    prev = 0
    current = 1

    if n == 1 :
      return 1
    
    # starts at 2nd term
    for _ in range(n - 1) : 
      temp = prev
      prev = current
      current += temp
    return current
