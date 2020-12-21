def is_prime(x):
  if x == 1:
    return False
  for i in range(2,x):
    if x % i == 0:
      return False
  else:
      return True
def print_primes_between(x,y):
  for i in range(x+1,y):
    if is_prime(i):
      print(i)
print_primes_between(0,50)