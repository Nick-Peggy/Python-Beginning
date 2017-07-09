#Author:Nick

data = {
    "重庆":{
        "渝北区":{
            "水晶郦城":["一组团","二组团"],
            "紫都城":["一单元","二单元"]
        },
        "江北区":{
            "围城国际公寓":["2801","2802"],
            "无专厂":["流星花园","锦瑟年华"]
        }
    },
    "北京":{
        "海淀区":["北京交通大学","中央民族大学"],
        "朝阳区":["蓝色港湾","三里屯"]
    },
    "香港":{
        "九龙":["港科大","坑口"],
        "香港岛":["中环","紫荆广场"]
    }
}

while True: #建立死循环
    for i in data:
        print(i) #打印第一级菜单
    choice = input("请选择1，或输入任意键退出：")
    if choice in data:
        while True:
            for j in data[choice]:
                print("\t", j) #打印第二级菜单
            choice2 = input("请选择2，或输入b返回上一级菜单：")
            if choice2 in data[choice]:
                while True:
                    for k in data[choice][choice2]:
                        print("\t\t", k) #打印第三级菜单
                    choice3 = input("请选择3，或输入b返回上一级菜单：")
                    if choice3 in data[choice][choice2]:
                        for z in data[choice][choice2][choice3]:
                            print("\t\t\t",z) #打印第三级菜单具体内容
                        print("这是最后一级菜单了，即将返回上一级菜单") #不用break，循环自动返回至上一级菜单
                    if choice3 == "b":
                        break #跳出循环，返回第二级菜单
            if choice2 == "b":
                break #跳出循环，返回第一级菜单
    else:
        break #结束程序
print("感谢使用小戴版三级菜单")