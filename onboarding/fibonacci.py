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
    #check if n is an integer and greater than 0
    #if not,raise TypeError
    if not isinstance(n,int) or n<=0:
        raise TypeError("n must be a positive integer")
    first=1
    second=1
    if n<=2:
        return 1
    for i in range(2,n):
      third=first+second
      first,second=second,third


    return third



    
