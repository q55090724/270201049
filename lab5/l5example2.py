  
x = int(input("How Many Numbers :"))
number_even = 0
number_odd = 0
for i in range(1,x+1):
  a = int(input("Enter a Number:"))
  if a % 2 == 0:
    number_even += 1
  elif a % 2 == 1:
    number_odd += 1

print((number_even /(number_even + number_odd)) * 100)