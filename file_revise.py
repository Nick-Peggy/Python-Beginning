#Author:Nick

f = open("yesterday","r",encoding="utf-8")
f_new = open("yesterday.bak","w",encoding="utf-8")
for line in f:
    if "那么多甜美的曲儿" in line:
        line = line.replace("那么多甜美的曲儿","那么少")
    f_new.write(line)

f.close()
f_new.close()
