first_password = "abc123"

x = input("Please Enter Your Password, (press help to get hint) :")

while x != first_password :
  print("Wrong")
  x = input("Enter Your Password Again: ")

if x == first_password :
  print("Welcome")

elif x == "help":
    print(first_password[0] + "*****")


