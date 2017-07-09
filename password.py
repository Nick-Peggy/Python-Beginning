#Author:Nick

_username = "daizhi"
_password = "123456" #输入正确的账号密码
username = input("username:")
password = input("password:")
if _username == username and _password == password:
    print("Welcome user %s login..." % (username)) #如果账号和密码都正确显示一段文字
else:
    print("invalid username or password!") #其他情况显示其他文字