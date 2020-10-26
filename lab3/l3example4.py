x = int(input("Please Enter Your Age for Ticket Prize : "))
y = 3.0
if x < 6 or x > 60 :
  print("FREE")

elif 6 < x < 18 :
  print("% 50 discount : ", (y*0.5))

else : 
  print("Ticket Cost : ", y)