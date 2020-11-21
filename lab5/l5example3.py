match = 0
digit = 0
x = (input("ENTER THE first NUMBER:"))
y = (input("ENTER THE second NUMBER:"))
x = list(x)
y = list(y)
x = list(reversed(x))
y = list(reversed(y))

while digit< len(x) and digit < len(y):
  if(x[digit]) == (y[digit]):
     match += 1
  digit += 1
print(match)




