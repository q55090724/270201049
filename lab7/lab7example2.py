books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}
for i in books:
  le = set(i)
  for letters in le:  
    book_dict.update({i:(len(i),len(le))})
print(book_dict)  
    





