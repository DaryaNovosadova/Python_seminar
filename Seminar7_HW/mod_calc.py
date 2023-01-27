from logg import logging
import excep
x = 0
y = 0
def init(a, b):
    global x
    global y
    x = a
    y = b
def init_x(a):
    global x
    x = a

def sum():
    return x + y

def sub():
    return x - y

def mul():
    return x * y

def div():
    return x / y

def div_c():
    return x // y

def div_o():
    return x % y

def pow():
    return x ** y

def sqrt():
    return x ** 0.5

x1 = 0
y1 = 0
x2 = 0
y2 = 0
def init_c1(a1, b1):
    global x1
    global y1
    x1 = a1
    y1 = b1

def init_c2(a2, b2):
    global x2
    global y2
    x2 = a2
    y2 = b2

xx = 0
yy = 0
def compl_x():
    xx = complex(x1, x2)
    return xx
def compl_y():
    yy = complex(y1, y2)
    return yy

def sum_compl(xx, yy):
    return xx + yy

def sub_compl(xx, yy):
    return xx - yy

def mul_compl(xx, yy):
    return xx * yy

def div_compl(xx, yy):
    return xx / yy


