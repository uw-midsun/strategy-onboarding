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
    def fib(n):
        if (n in (0,1)):
            return n
        return fib(n-1) + fib(n-2)
    if (isinstance(n,int) and n>=1):
        return fib(n)
    raise TypeError
