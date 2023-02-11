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
    if (n <= 0):
        raise(TypeError)

    A = []
    # adding the initial 2 elements
    A.append(0) 
    A.append(1)

    # hence, loop from 2 onwards
    for i in range(2, n+1) :
        A.append(A[i-1] + A[i-2])
    
    return A[n]