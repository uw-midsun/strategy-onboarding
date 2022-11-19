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
    n1 = 1
    n2 = 1
    fib = 0
    count = 0
    listfib = []

    if n <= 0:
      raise TypeError("Input is too small must be above zero")

    if not isinstance(n, int):
      raise TypeError("Input must be integer above zero")



    if n == 1 or n == 2:
      return 1


    while count < n:
      n1 = n2
      n2 = fib
      fib = n1 + n2
      listfib.append(fib)
      count += 1
    else:
      return listfib[n-1]

