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
    pass
    n1 = 1
    n2 = 1
    fib = 0
    count = 0
    listfib = []
    if n == 1 or n == 2:
      print("your value is 1")
      return 1

    while count < n:
      n1 = n2
      n2 = fib
      fib = n1 + n2
      listfib.append(fib)
      count += 1
    else:
      print("Your value is " + str(listfib[n-1]))
      return listfib[n-1]


