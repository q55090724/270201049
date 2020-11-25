x = input("Please Enter Your Email Adress :")
t = "ceng113@example.com"
z = (t.split("@")[0]).upper()
y = (t.split("@")[0]).replace('','.')
previous_ = x.split("@")[0]
after_ = x.split("@")[1]
while True:
  if x == t:
    print("True")
    break
  elif z == previous_:
    print("True")
    break
  elif previous_ ==  y :
    print("True")
    break
  else:
    print("Wrong")
    x = input("Please Enter Your Email Adress Again:")

  
  
