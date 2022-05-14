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
    # Invalid Number
    if (n <= 0):
      raise(TypeError)
    # n = 1 and n = 2 case
    if n == 1 or n == 2:
      return 1

    # Rest of the cases from 2 - inf
    fibarr = [1,1]
    for i in range(0,n-2):
      fibarr.append(fibarr[len(fibarr)-1] + fibarr[len(fibarr)-2])
      
    return fibarr[len(fibarr)-1]