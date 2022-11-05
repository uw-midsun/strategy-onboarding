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
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    n1 = 0
    n2 = 1
    for i in range(2,n):
      sum = n1 + n2
      n1 = n2
      n2 = sum
      
  return(n2)