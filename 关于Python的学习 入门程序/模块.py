 # Python模块(module):一个.py文件就是一个模块，模块是Python程序的基本组织单位。在模块中可以定义变量，函数，类，以及可以执行的代码
 #可以提高代码复用 ,降低开发门槛 ，避免命名冲突

 # 模块导入方式
 #在使用模块中提供的功能之前，必须得先导入，再使用
 #导入模块的具体语法如下:
 # import 模块名                             import random,os(多个模块之间用,分割)          模块名.功能名        random.randint(10.100)
 # import 模块名 as 别名                      import random as rd                        别名.功能名          rd.randint(10,100)
 # from 模块名 import 功能名                  from random import randint,choice           功能名              randint(10,100)
 # from 模块名 import 功能名 as 别名           from random import randint as rint          别名               rint(10,100)
 # from 模块名 import *                      from random import *                        功能名              randint(10,100)
 #前面两种方法是导入整个模块 后面三种方法是导入模块中的一部分功能 最后一个是导入模块中的全部功能

#例如:
import random
for i in range(100):
    print(random.randint(1,1000))#随机生成1到1000之间的数包含1000

# 自定义模块 当一些复杂的项目，为了让项目的结构更清晰，更便于项目的维护及代码的复用 ， 可能会把一个项目拆分为诺干个模块
#每一个Python文件都可以作为一个模块，模块的名字就是文件的名字(建议使用Python标识符定义，规范命名)
# 测试函数   __name__   Python中的内置变量，表示当前模块的名字(直接运行当前模块， __name__的值为str "__nain__";当该模块被导入时，__name__的值就是模块名)
#可以用if语句和__name__ == __nain__ 来执行测试代码

# __all__是一个模块级别的特殊变量，用于指定 from 模块名 import * 时会导入哪些功能(*通配啦哪些功能)
#如 __all__ = ["模块名1","模块名2"]  要以str形式出现 且是在模块文件中定义的 因此在目标代码中 * 代表的就是__all__中的功能
#注意:__all__控制的是from ... import * 时，要导入的功能，并不会直接影响导入具体的功能(如:from ... import 功能)


#软件包 :绷直就是一个文件夹，该文件夹中可以包含若干Python模块(.py文件)，文件夹下还包含了一个__init__.py(描述当前包的信息)
#作用:模块比较多的时候，用开管理多个模块(包的本质也是一个模块)
# import 包名.模块名             import  utils.my_fun                      包名.模块名.功能名         utils.my_fun.long_sepaeator1()
# from 包名 import 模块名        from  utils import my_fun                 模块名.功能名              my_fun.long_sepaeator2()
# from 包名 import *            from  utils import *                      模块名.功能名              my_fun.long_sepaeator3()
# from 包名.模块名 import 功能名  from  utils.my_fun import log_separator1  功能名                    log_separator1
# from 包名.模块名 import *      from  utils.my_fun import *               功能名                    log_separator1
#注意:如果要通过from 包名 import * 这种方式导入包下的所有模块，需要__init__.py 文件中添加 __all__=[] 同样__all__中的模块也要以str的形式