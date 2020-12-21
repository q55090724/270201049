def harmonic(x):
  if x == 1:
    return 1
  return (1/x) + harmonic(x-1)

a = int(input("Enter an integer for harmonic sum : "))

print(harmonic(a))