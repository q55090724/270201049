import random
def get_rand_list(b=0,e=10,N=5):
  list1 = []
  for x in range(N):
    list1.append(random.randint(b,e))
  return list1
a = get_rand_list(b=0,e=10,N=5)
def get_overlap(listx,listy):
  listz = []
  print(listx)
  print(listy)
  for i in listx:
    if i in listy:
      listz.append(i)
  return listz
print(get_overlap(get_rand_list(b=0,e=10,N=5),get_rand_list(b=0,e=10,N=5)))

























