#Author:Nick

goods_list = [["towel",20],["tissue",10],["food",25],["water",5]]
salary = int(input("Please input your salary:")) #输入工资，强制转换格式为整型
balance = salary
cart = []
while True:
    for index,item in enumerate(goods_list):
        print(index,item) #打印商品编号及价格
    x = int(input("Please type item number:")) #输入想要购买的商品编号
    if balance >= goods_list[x][1]: #判断余额是否大于商品价格
        balance = balance - goods_list[x][1]
        print("\033[31;1mbalance\033[0m:",balance) #\033[31;1m%s\033[0m 高亮显示31表示红色，32表示绿色
        cart.append(goods_list[x][0])  #将购买的商品名称插入到cart列表中
    else:
        print("Insufficient balance!") #若余额不足，则提醒
    continue_res = input("Do you want to buy more item? Y/N:")
    if continue_res == "N": #判断是否继续购物
        break
print(cart,"\n","\033[32;1mbalance\033[0m:",balance) #打印商品购买清单和余额



