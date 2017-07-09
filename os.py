#Author:Nick
import os
#cmd_res = os.system("dir") #显示当前磁盘目录下的所有文件
cmd_res = os.popen("dir").read()
print("-->",cmd_res)
os.mkdir("new!") #在当前目录下创建新目录