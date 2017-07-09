#Author:Nick
'''
names = ['Nick','Peggy','Samantha']
print(names)
print(names[0]) #下标从0开始计数
print(names[1])
print(names[2])
print(names[-1]) #也可以倒着取值
print(names[-2])

names = ['Alex', 'Tenglan', 'Eric', 'Rain', 'Tom', 'Amy']
print(names)
names.remove("Alex") #直接指定元素删除
print(names)
del names[3] #通过下标删除
print(names)
names.pop() #删除最后一个元素
print(names)

a = [1,2,3,4]
b = [33,45,2]
a.extend(b)
print(a)

names = ['Alex', 'Tenglan', 'Eric', 'Rain', 'Tom', 'Amy']
print(names)
print(names.index("Eric")) #只返回找到的第一个下标

names = ['Alex', 'Amy','Tenglan', 'Eric', 'Rain', 'Tom', 'Amy']
print(names.count('Amy'))
'''
names = []
names.insert(0,"Alex")
print(names[0])

for i in range(1,6):
    print(i)








