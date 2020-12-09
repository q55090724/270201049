numbers1 = [2,3,4,20,5,5,15]
numbers2 = [10,20,20,15,30,40]
numbers1_set = set(numbers1)
numbers2_set = set(numbers2)
intersection_ = []
print(numbers1_set)
print(numbers2_set)
for i in numbers1_set:
    if i in numbers2_set:
        intersection_.append(i)
print("Intersection",intersection_)
union_ = numbers2_set.copy()
union_ = list(union_)
for i in numbers1_set:
    if i not in numbers2_set:
        union_.append(i)
print("Union",union_)