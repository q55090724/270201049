c = 0 
employees = {}
salaries = []
while c < 5:
  x = input("Please Enter Employee's Name:")
  y = int(input("Enter Salary: "))
  employees.update({x:y})
  c+=1
a = employees.items()
for name,sal in a:
  salaries.append(sal)
salaries.sort()
salaries.remove(salaries[0])
salaries.remove(salaries[0])
for name, age in employees.items():
  for i in salaries:
    if i == age:
      print(name)




  
  
    

