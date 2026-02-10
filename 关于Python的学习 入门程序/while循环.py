# while 条件表达式:
#     循环体1
#     循环体2
#     ...
#else:
#   条件为False，循环正常结束时执行
# 还可在while语句后加入else，如上所示
# num = int(input("请输入你要循环的数"))
# while num<=10:
#     print(num)
#     num=num+1
# else:
#     print(num)



#案例 计算0到100之间的所有偶数之和
js = 0
num = 0
while num<=100:
    num +=1
    if num%2==0:
        js+=num
else:
    print(js)