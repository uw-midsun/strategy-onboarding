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
    if (n <= 0 or type(n) != int):
        raise TypeError

    #had this initally but had to fit the requirements in the test case
    # if n == 0:
    #   return 0

    #base case
    if n == 1:
      return 1

    #to catch when fib(0) is called, we can then understand that this is when n = 2, which is 1
    if(n-2 == 0):
      return 1

    #fibonacci sequence is defined as fib(n) = fib(n-1) + fib(n-2)
    return fibonacci_term(n-1) + fibonacci_term(n-2)

    pass

# print(fibonacci_term(k))
