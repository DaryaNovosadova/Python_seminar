from logg import logging
import excep
def menu():
    while True:
        num_type = input('Enter:\n'
                        '1 - rational\n'
                        '2 - complex\n'
                        '0 - exit\n')
        match num_type:
            case '1':
                logging.info('menu item selected rational')
                menu_rational()
            case '2':
                logging.info('menu item selected complex')
                menu_complex() 
                
            case '0':
                logging.info('Stop program')
                break
            case _:
                logging.warning('main menu wrong iteme selected')
                print('Err')


def menu_rational():
    while True:
        operation = input('1 - sum"+"\n'
                        '2 - sub"-"\n'
                        '3 - mul"*"\n'
                        '4 - div"/"\n'
                        '5 - pow"a^b"\n'
                        '6 - sqrt"\/a"\n'
                        '0 - previous menu\n')
        match operation:
            case '1':
                logging.info('rational menu item selected sum')
                excep.go_calcSum()
            case '2':
                logging.info('rational menu item selected sub')
                excep.go_calcSub()
            case '3':
                logging.info('rational menu item selected mul')
                excep.go_calcMul()
            case '4':
                logging.info('rational menu item selected div')
                menu_div()
            case '5':
                logging.info('rational menu item selected pow')
                excep.go_calcPow()
            case '6':
                logging.info('rational menu item selected sqrt')
                excep.go_calcSqrt()
            case '0':
                logging.info('return to the main menu')
                menu()
def menu_div():
    while True:
        operation = input('1 - div"/"\n'
                        '2 - inDiv"//"\n'
                        '3 - remOfDiv"%"\n'
                        '0 - previous menu\n')
        match operation:
            case '1':
                logging.info('division menu item selected div')
                excep.go_calcDiv_1()
            case '2':
                logging.info('division menu item selected integer div')
                excep.go_calcDiv_2()
            case '3':
                logging.info('division menu item selected remainder of div')
                excep.go_calcDiv_3()
            case '0':
                logging.info('return to the previous menu')
                menu_rational()

def menu_complex():
    while True:
        operation = input('1 - sum"+"\n'
                        '2 - sub"-"\n'
                        '3 - mul"*"\n'
                        '4 - div"/"\n'
                        '0 - previous menu\n')
        match operation:
            case '1':
                logging.info('complex menu item selected sum')
                excep.go_calc_Sum()
            case '2':
                logging.info('complex menu item selected sub')
                excep.go_calc_Sub()
            case '3':
                logging.info('complex menu item selected mul')
                excep.go_calc_Mul()
            case '4':
                logging.info('complex menu item selected div')
                excep.go_calc_Div()
            case '0':
                logging.info('return to the main menu')
                menu()


menu()