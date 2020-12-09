x = int(input("Enter Number : "))
y = ["0"]
y = x * y
c = ""
for i in range (0,x):
  y[i] = "1"
  for i in y:
    c = c + i
  print(c,sep="")
  c = ""
  y = ["0"]
  y = x * y
  
