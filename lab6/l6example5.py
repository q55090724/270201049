x = int(input("Enter Number : "))
y = ["0"]
y = x * y
c = ""
for i in range (0,x):
  y[i] = "1"
  for p in y:
    c = c + p
  print(c)
  c = ""
  y = ["0"]
  y = x * y
  
