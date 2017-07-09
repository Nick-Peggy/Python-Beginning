#Author:Nick

list_1 = [1,4,5,5,2,3,5]
list_1 = set(list_1)
list_2 = set([2,5,3,1,2,3,5,6])
print(list_1,list_2)

print(list_1.intersection(list_2))
print(list_1 & list_2) #交集

print(list_1.union(list_2))
print(list_1 | list_2) #并集

print(list_1.difference(list_2))
print(list_1 - list_2) #差集

print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2) #对称差集

list_3 = set([1,4,5])
print(list_3.issubset(list_1)) #判断是否为其子集
print(list_1.issuperset(list_3)) #判断是否为其父集

list_3.remove(4) #删除一项元素，如果该元素不在集合中，报错
print(list_3)

list_3.discard(1) #删除一项元素，如果该元素不在集合中，不作任何处理
print(list_3)


