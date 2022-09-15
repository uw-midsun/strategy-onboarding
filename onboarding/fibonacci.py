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


    if n<=0:
      raise TypeError('Invlad for length under 0')


    if n==1 or n == 2:
      return 1
    
    sum = [1,1]

    for j in range(2,n):
      sum.append(sum[j-1] + sum[j-2])

    return sum[len(sum)-1]


    # insert code here
    pass
