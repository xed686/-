# 字面量：指程序中，直接书写的固定值（数据），就称为字面量
print(100)#整数int
print(3.14)#浮点数float布尔类型本质上也是整数类型
print(True)#布尔（bool）
print(False)#布尔（bool）
print("Hoola Python")#字符串（str）
print("------------")#字符串（str）
print(None)#空值(NoneType)
# 通过type()语句来得到数据的类型，具体语法为：type(要查看类型的数据)
print(type("Hello World"))
print(type(10))

num=1.0
print(type(num))

# 通过isinstance()检查函数是否属于指定的类型，返回一个bool值，具体语法为：isinstance(检查数据,目标类型)
num=5.0
print("num")
print(isinstance(num,int))