# 通过%占位符的形式来完成字符串和变量的快速拼接（其中%表式我要占位，s表示将变量放入占位符的位置）
# s1="涛哥"
# print("大家好，我是%s，欢迎大家进入Python的学习" % s1)
from pickletools import string1

s1=("人生苦短")
s2=("我用Python")
print("吉多 范罗苏姆：%s,%s"%(s1,s2))
# 也可以通过f"内容{变量/表达式}"的形式来完成快速格式化
name = "涛哥"
print(f"大家好，我是{name}，欢迎大家进入Python的学习")
print(f"吉多 范罗苏姆： {s1}，{s2 }")