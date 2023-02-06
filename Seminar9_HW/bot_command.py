from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logg import logging

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('Hi. Menu')
    await update.message.reply_text(f'Hi {update.effective_user.first_name}\n Выбирай:\n 1 - рациональные\n 2 - комплексные')

async def rac_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('menu item selected rational')
    await update.message.reply_text(f'Выбирай (после ввода пункта меню, вводи сразу цифры через пробел):\n3 - сумма\n'
                                    '4 - вычитание\n'
                                    '5 - умножение\n'
                                    '6 - деление\n'
                                    '7 - возведение в степень\n'
                                    '8 - квадратный корень\n'
                                    '0 - вернуться назад')

async def com_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('menu item selected complex')
    await update.message.reply_text(f'Выбирай (после ввода пункта меню, вводи сразу цифры через пробел):\n9 - сумма\n'
                                    '10 - вычитание\n'
                                    '11 - умножение\n'
                                    '12 - деление\n'
                                    '0 - вернуться назад')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('rational menu item selected div')
    await update.message.reply_text(f'Выбирай (после ввода пункта меню, вводи сразу цифры через пробел):\n13 - простое деление\n'
                                    '14 - целочисленное деление\n'
                                    '15 - остаток от деления\n'
                                    '0 - вернуться назад')

