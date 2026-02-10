# 打印一个长为m,宽为n的矩形
# m =int(input("请输入宽"))
# n =int(input("请输入长"))
# for i in range(1,m+1):
#     for k in (1,n+1):
#         print("*",end=" ")
#     print()
#如果想要快速换行 就按下shift加回车  其中print语句自带换行效果print("*",end="") end表示的是每一次输出以什么结束；默认\n，当end="\n"表示换行，当里面什么都不写的时候表示在一行中按序输入
#当你想在*号后面加上空格时，可以在den=""里面加上空格


# 案例 输出99乘法表
# i = int(input(""))
# k = 1
# while k<=i:
#     for n in range(1,k+1):
#         if n*k >= 10:
#             print(f"{n}*{k}={n*k} ",end="")
#         else:
#             print(f"{n}*{k}={n*k}  ",end="")
#     print()
#     k = k+1

# 根据输入的直角边的边长 打印直角三角形
i= int(input("请输入直角边的边长"))
k=1
for n in range(1,i+1):
    for m in range(1,n+1):
        print(f"* ",end="")
    print()
#只能出现在循环的关键字break       表示结束，跳出循环的意思
#只能出现在循环中的关键字continue  表示中断本次循环，直接进入下一次循环


#生成随机数
# import random
# random_num = random.randint(a=1 , b=100)#随机生成一个1到100的数
