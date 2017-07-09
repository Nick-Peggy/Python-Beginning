#Author:Nick

import sys,time
for i in range(100):
    sys.stdout.write("#") #一个个输出#号
    sys.stdout.flush() #刷新内存
    time.sleep(0.5) #延迟处理