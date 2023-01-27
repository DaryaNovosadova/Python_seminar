from logg import logging
import excep
import mod_calc

def data(result):
    print(f'Result = {result}')

def init_a():
    while True:
        try:
            a = float(input('Enter a '))
            logging.info(f'data received {a}')
            return a
        except ValueError:
            logging.warning('invalid value entered')
            print('Enter number!')


def init_b():
    while True:
        try:
            b = float(input('Enter b '))
            logging.info(f'data received {b}')
            return b
        except ValueError:
            logging.warning('invalid value entered')
            print('Enter number!')

def go_calcSum():
    a = init_a()
    b = init_b()
    mod_calc.init(a, b)
    result = mod_calc.sum()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calcSub():
    a = init_a()
    b = init_b()
    mod_calc.init(a, b)
    result = mod_calc.sub()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calcMul():
    a = init_a()
    b = init_b()
    mod_calc.init(a, b)
    result = mod_calc.mul()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calcDiv_1():
    a = init_a()
    b = init_b()
    mod_calc.init(a, b)
    result = mod_calc.div()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calcDiv_2():
    a = init_a()
    b = init_b()
    mod_calc.init(a, b)
    result = mod_calc.div_c()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calcDiv_3():
    a = init_a()
    b = init_b()
    mod_calc.init(a, b)
    result = mod_calc.div_o()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calcPow():
    a = init_a()
    b = init_b()
    mod_calc.init(a, b)
    result = mod_calc.pow()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calcSqrt():
    a = init_a()
    mod_calc.init_x(a)
    result = mod_calc.sqrt()
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calc_Sum():
    a1 = init_a()
    b1 = init_b()
    a2 = init_a()
    b2 = init_b()
    mod_calc.init_c1(a1, b1)
    mod_calc.init_c2(a2, b2)
    xx = mod_calc.compl_x()
    yy = mod_calc.compl_y()
    result = mod_calc.sum_compl(xx, yy)
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calc_Sub():
    a1 = init_a()
    b1 = init_b()
    a2 = init_a()
    b2 = init_b()
    mod_calc.init_c1(a1, b1)
    mod_calc.init_c2(a2, b2)
    xx = mod_calc.compl_x()
    yy = mod_calc.compl_y()
    result = mod_calc.sub_compl(xx, yy)
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calc_Mul():
    a1 = init_a()
    b1 = init_b()
    a2 = init_a()
    b2 = init_b()
    mod_calc.init_c1(a1, b1)
    mod_calc.init_c2(a2, b2)
    xx = mod_calc.compl_x()
    yy = mod_calc.compl_y()
    result = mod_calc.mul_compl(xx, yy)
    excep.data(result)
    logging.info(f'Result = {result}')

def go_calc_Div():
    a1 = init_a()
    b1 = init_b()
    a2 = init_a()
    b2 = init_b()
    mod_calc.init_c1(a1, b1)
    mod_calc.init_c2(a2, b2)
    xx = mod_calc.compl_x()
    yy = mod_calc.compl_y()
    result = mod_calc.div_compl(xx, yy)
    excep.data(result)
    logging.info(f'Result = {result}')




