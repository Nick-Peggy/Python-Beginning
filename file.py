#Author:Nick
"""
f = open("yesterday",encoding="utf-8") #得到文件句柄，即文件的内存对象，可以对文件进行操作
data = f.read() #读第一遍时从最头开始读
data2 = f.read() #读第二遍时从末尾开始读
print(data)
print("------------data2------------","\n",data2) #data2什么都没有

f.close()

data = open("yesterday",encoding="utf-8").read() #也可以直接读文件
print(data)
for index,line in enumerate(f.readlines()): #预先将文件内容一行行转成列表，并读下标和内容
    print(line.strip()) #去除空格和换行
    if index ==9:
        break #读前十行

f = open("yesterday",encoding="utf-8")
count = 0
for line in f:
    print(line.strip())
    count += 1
    if count == 10:
        break
f = open("yesterday",encoding="utf-8")
print(f.tell())
print(f.read(5))
print(f.tell())
print(f.fileno())
print(f.seekable())
print(f.flush())
"""
f = open("yesterday","w+",encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.tell())
f.write("------------------")
print(f.readline())





