x = int(input("Enter Number of Students: "))

total = 0
av_grade_list = []
for i in range(x):
  a = int(input("Enter Midterm 1 Grade:"))
  b = int(input("Enter Midterm 2 Grade:"))
  c = int(input("Enter Final Grade:"))

  a = a * (3/10)
  b = b * (3/10)
  c = c * (4/10)

  total = a + b + c
  if total > 90:

   av_grade_list.append(total)

  

print(av_grade_list)





