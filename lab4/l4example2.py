x = int(input("Please Enter a Year : "))

if x % 100 == 0 and x % 400 == 0:
  print("Leap Year")
elif x % 100 == 0:
  print("Not a Leap Year")
elif x % 4 == 0:
  print("Leap Year")
else:
  print("Not a Leap Year")
