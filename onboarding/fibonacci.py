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

    counter=1
    firstnum=0
    secondnum=1
    answer=0
    if (n<=0):
      raise TypeError("not a positive integer")
    if (n==1):
        return (1)
    while (counter<n):
      answer=firstnum+secondnum
      if (counter%2!=0):
        firstnum=answer
      else:
        secondnum=answer 
      counter+=1
    return(answer)      




