def fibonacci_term(n):
    '''
    @params n: integer
    @returns integer, nth term of the Fibonacci sequence
    '''

    if (n <= 0):
      raise TypeError
    
    x = 0
    n1 = 1
    n2 = 1

    if (n==1 or n==2):
      x = 1
    else:
      for i in range(2,n):
        x = n1 + n2
        n2 = n1
        n1 = x
        

    return x
