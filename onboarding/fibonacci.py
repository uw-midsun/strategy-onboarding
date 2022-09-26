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
      raise TypeError()
    fib_array = [0, 1]
    for i in range(n):
      fib_array.append(fib_array[i] + fib_array[i+1])
    return fib_array[n]