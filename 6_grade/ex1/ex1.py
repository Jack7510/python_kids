# -*- coding: utf-8 -*-
#!/usr/bin/python3

import os
#from jack_ex import *
from exercise import *

def test_exercise():
    print("Python编程练习测试...")

    print("\n\n题目1: 实现数学公式... 期望结果 462")
    print("实际结果：%d" % calc_polynomial(2,3,4,5,6))
    raw_input("敲 Enter 键继续...")

    print("\n\n题目2: 字符串乘法... 期望结果 HelloHelloHello ")
    print("实际结果：%s" % str_times('Hello', 3))
    raw_input("敲 Enter 键继续...")

    print("\n\n题目3: 返回字符串中第n个字母... 期望结果 C ")
    print("实际结果：%c" % str_get_char('ABCDEFG', 2))
    raw_input("敲 Enter 键继续...")

    print("\n\n题目4: 把新来同学Jobs的名字加入到名单中 期望结果 ['Jack', 'Bill', 'Peter', 'Jobs'] ")
    names = ['Jack', 'Bill', 'Peter']
    str_list_add(names, 'Jobs')
    print("实际结果："); print( names )
    raw_input("敲 Enter 键继续...")

    print("\n\n题目5: 把离开的同学Jobs的名字从到名单中['Jack', 'Bill', 'Peter', 'Jobs']删除 期望结果 ['Jack', 'Bill', 'Peter'] ")
    names = ['Jack', 'Bill', 'Peter', 'Jobs']
    str_list_del(names, 'Jobs')
    print("实际结果："); print( names )
    raw_input("敲 Enter 键继续...")

    print("\n\n题目6: 有一个字典，保存了同学的名字和他对应的体重，输入姓名，返回同学的体重，预期结果 130 ")
    classmates = {'Jack':130, 'Bill':140, 'Margret':120, 'Qiu':60}
    
    print("实际结果："); print( map_key_val(classmates, 'Jack') )
    raw_input("敲 Enter 键继续...")

    print("本次练习结束...Bye")
    return


if __name__ == '__main__':
    test_exercise()
