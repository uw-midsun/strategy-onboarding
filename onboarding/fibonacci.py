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
    if n < 1 or not isinstance(n, int):
        raise TypeError()

    curr = 1
    prev = 0
    for i in range(n - 1):
        next = curr + prev
        prev = curr
        curr = next
    print(curr)
    return curr
