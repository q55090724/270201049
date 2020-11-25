x = int(input("Please Enter Number of Items :"))
y = []
for i in range(x):
  a = input("Enter Item :")
  y.append(a)
z = set(y)
z = list(z)
z.sort()
print(z[::-1])


