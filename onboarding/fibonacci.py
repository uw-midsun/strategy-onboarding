def fibonacci_term(n):
    if n <= 0:
        raise(TypeError)
    return fib_acc(0,1,n)

def fib_acc(prev, curr, n):
    if n == 1:
        return curr
    return fib_acc(curr, prev+curr, n-1)