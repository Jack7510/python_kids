#!/usr/bin/env python3
from tkinter import *


# 常用数字和操作符的列表
legal_char  = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
    '+', '-', '=', '*', '/', '^', '\x08', '\x7f', '\r']
calc_op     = ['*', '/', '+', '-', '^']
nums        = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def eval_proc(str_exp):
    '''
    完成输入算式的运算，并返回结果

    参数：
    str_exp     - 输入的算术表达式

    返回:    运算结果
    '''
    try:
        # 把 ^ 替换为**，Python中的幂运算
        str_exp = str_exp.replace('^', '**')
        print(str_exp)
        ans = eval(str_exp)
    except Exception as ex:
        str_exp = '计算错误'
    else:
        #print(calc_str)
        ans = round(ans, 10)
        str_exp = str(ans)
        str_exp = str_exp[0:10]
    return str_exp


def backspace_proc(str):
    '''
    处理删除键，删掉算术表达式的最后一个字符

    参数：
    str     - 输入的算术表达式

    返回：   删除最后一个字符
    '''
    if str[0] not in legal_char:
        str = '0'
    else:
        str = str[0: len(str)-1]
        if str == '':
            str = '0'

    return str

def minus_op_proc(str):
    '''
    正负号的处理，把整数改为负数，把负数改为正数

    参数：    算术表达式
    返回：    一个数的相反值
    '''
    if str[0] == '-':
        str = str[1:]
    else:
        str = '-' + str
    
    return str


def num_op_proc(str, key):
    '''
    数字和操作符处理，把他们添加到表达式中

    参数：      
    str         - 目前的算术表达式

    返回： 处理后的新表达式
    '''

    # 如果表达式是'0'，就是空的，或者是'计算错误‘, 则直接替代为输入的数字
    if (str == '0' or (str[0] not in legal_char)) and key in nums:
        str = key

    elif str == '0.' and key in nums:
        str = key

    else:
        # 如果最后一个是运算符，输入的也是运算符，就用新的运算符替代
        if key in calc_op and str[-1] in calc_op:
            str = str[0: len(str)-1] + key
        else:
            # 把新输入的数字或者运算符加在最后
            str += key

    return str


def calc_core2(key, calc_expr):
    '''
    处理用户输入，构成有效的算术表达式，并执行结果
    
    参数：  
    key         - 用户输入的按键
    calc_expr   - 输出框的控件

    返回：      - 无
    '''
    global calc_str

    if key == '=' or key == '\r':
        # 执行算术运算
        print(calc_str)
        calc_his.set(calc_str + '=')
        calc_str = eval_proc(calc_str)

    elif key == 'C' or key == '\x08' or key == '\x7f':
        # 处理删除键
        calc_str = backspace_proc(calc_str)

    elif 'AC' == key:
        # 处理清除键
        calc_str = '0'
    
    elif '±' == key:
        # 处理相反数
        calc_str = minus_op_proc(calc_str)

    else:
        if '÷' == key:
            key = '/'
        elif '×' == key:
            key = '*'

        # 处理有效数字和运算符
        calc_str = num_op_proc(calc_str, key)

    calc_expr.set(calc_str)


#
# 按钮事件处理
#
def click_event(key, calc_expr):
    #print(key)
    calc_core2(key, calc_expr)


#
# 键盘事件处理函数
#
def key_proc(event, calc_expr):
    print('pressed', repr(event.char))
    calc_core2(event.char, calc_expr)


#def main():
#global calc_str

# 建立tk窗口
calc = Tk()
calc.title("My Calc")

# 创建计算公式的输入栏
calc_str = '0'
calc_expr = StringVar()
calc_expr.set(calc_str)
display = Label(calc, width=10, height=1, bg='white', textvariable=calc_expr,
                justify=RIGHT, anchor=E, font=("Helvetica", 40))
display.grid(row=1, column=0, columnspan=4)

# 创建计算公式的历史栏
calc_his = StringVar()
calc_his.set('')
display_his = Label(calc, width=10, height=1, bg='white', textvariable=calc_his,
                justify=RIGHT, anchor=E, font=("Helvetica", 40))
display_his.grid(row=0, column=0, columnspan=4)

# 创建和计算器相关的按键
buttons = [
    'C', 'AC', '^', '÷',
    '7', '8', '9', '×', 
    '4', '5', '6', '-', 
    '1', '2', '3', '+', 
    '0', '.', '±', '='
]

row = 2
col = 0
for i in buttons:
    action = lambda x = i: click_event(x, calc_expr)
    Button(calc, text=i, width=3, height=2, command=action, font=("Helvetica", 20), padx=0) \
        .grid(row = row, column = col, sticky = 'nesw', )
    col += 1
    if col > 3:
        col = 0
        row += 1

# 捕获键盘输入
calc.bind('<Key>', lambda e: key_proc(e, calc_expr))

mainloop()

