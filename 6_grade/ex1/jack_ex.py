# -*- coding: utf-8 -*-

""" 同学们，请根据文档把作业填在下面的各个函数
"""

""" 热身练习，一个最简单的Python函数, 把两个字符串连在一起
"""
def joint_2_string(a, b):
    return a + b


""" 练习1：计算多项式的值，数学公式看文档
"""
def calc_polynomial(a, b, c, x, y):
    sum = 0
    # 在这里添加你代码
    sum = a + b * x + c * y + x ** 2 + y ** 3 + x * (y ** 2)
    return sum


# 练习 2
# 函数将输入一个字符串变量str和次数变量n，把str重复n次
# str  -- 字符串变量
# n    -- 重复次数
def str_times(str, n):
    new_str = ""

    # 在这里添加你代码
    new_str = str * n
    return new_str


"""
  练习 3 
  返回字符串中第n个字母

"""
def str_get_char(str, n):
    c = 0

    # 在这里添加你代码
    c = str[n]
    return c


"""
  练习 4
  把新来的同学名字 jobs_name 添加到班级的名字列表names中
  names     - 班级名称列表
  jobs_name - 新同学名字 
"""
def str_list_add(names, jobs_name):
    # 在这里添加你代码
    names.append(jobs_name)
    return names


"""
  练习 5
  你们班有个同学去其他学校了，需要把他的名字从你们的名字列表中删掉
  names     - 班级名称列表
  classmate - 离开同学的名字 
"""
def str_list_del(names, classmate):
    # 在这里添加你代码
    names.remove(classmate)
    return


"""
  练习 6 map
  有一个map，保存了同学的名字和他对应的体重，输入姓名，返回同学的体重
  maps      - 班级的体重表['姓名', 体重]
  name      - 同学的名字 
"""
def map_key_val(maps, name):
    weight = 0

    # 在这里添加你代码
    weight = maps[name]
    return weight
