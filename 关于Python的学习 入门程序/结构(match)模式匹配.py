# 结构模式匹配就是用一个清晰的模板去精准的匹配数据的结构和内容，匹配成功则执行响应的操作
# 所需要用到的语法就是match...case
#工作日安排
from unittest import case

day = input("请输入星期几（1——7）")
match day:
    case "1":
        print("周一:工作会议日")
    case "2":
        print("周二：学习培训日")
    case "3":
        print("周三：项目开发日")
    case "4" | "5" :# | 表示或的意思
        print("休息日")
    case _:# _ 表示除此之外的其他情况
        print("输入错误")
#也可以在case后面加条件判断语句if 意为当条件成立时才匹配语句
#match...case的应用场景
#natch基于应用的多个固定值进行分支判断时，可以使用match模式匹配
#if：条件判断涉及复杂的逻辑判定 范围比较及组合条件时