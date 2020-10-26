x = float(input("Please Enter Your GPA : "))
y = float(input("Please Enter Your Number of lectures : "))
if x < 2.0 and y < 47 :
  print("Not Enough Number of Lectures And GPA")
elif x >= 2.0 and y < 47 :
  print("Not Enough Number  of Lectures")
elif x < 2.0 and y >= 47 :
  print("Not Enough GPA")
else :
  print("GRADUATED")