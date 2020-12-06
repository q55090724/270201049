books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
  a = len(i)
  le = set(i)
  for letters in le:  
    book_dict.update({i:(a,len(le),(a + len(le))/2)})
print(book_dict)  

