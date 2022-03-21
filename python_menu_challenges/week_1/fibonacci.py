#WHAT IS THE FIBONACCI'S SEQUENCE
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

def run_fib_sum():

  list = []
  
  def fib(i):
    if(i < 0):
      return 0
    if( (i == 0) or (i == 1) ):
      list.append(1)
    else:
      list.append(list[i-1] + list[i-2])
  
  def get_sum(n):
    for i in range (n):
      fib(i) 
    sum = 0
    for i in range(n):
      sum += list[i]
    print(sum)
    
  n = int(input("n = "))
  get_sum(n)

run_fib_sum()