from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logg import logging

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('rational menu item selected sum')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    logging.info(f'received {x}, {y}')
    await update.message.reply_text(f'{x} + {y} = {x + y}')
    logging.info(f'result {x + y}')

async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('rational menu item selected sub')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    logging.info(f'received {x}, {y}')
    await update.message.reply_text(f'{x} - {y} = {x - y}')
    logging.info(f'result {x - y}')

async def mul_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('rational menu item selected mul')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    logging.info(f'received {x}, {y}')
    await update.message.reply_text(f'{x} * {y} = {x * y}')
    logging.info(f'result {x * y}')

async def divP_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('division menu item selected div')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    logging.info(f'received {x}, {y}')
    await update.message.reply_text(f'{x} / {y} = {x / y}')
    logging.info(f'result {x / y}')

async def divC_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('division menu item selected integer div')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    logging.info(f'received {x}, {y}')
    await update.message.reply_text(f'{x} // {y} = {x // y}')
    logging.info(f'result {x // y}')

async def divO_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('division menu item selected remainder of div')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    logging.info(f'received {x}, {y}')
    await update.message.reply_text(f'{x} % {y} = {x % y}')
    logging.info(f'result {x % y}')

async def pow_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('rational menu item selected pow')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    y = float(items[2])
    logging.info(f'received {x}, {y}')
    await update.message.reply_text(f'{x}^{y} = {x ** y}')
    logging.info(f'result {x ** y}')

async def sqrt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('rational menu item selected sqrt')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = float(items[1])
    logging.info(f'received {x}')
    await update.message.reply_text(f'\/{x} = {x ** 0.5}')
    logging.info(f'result {x ** 0.5}')



async def comSum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('complex menu item selected sum')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[1])
    y2 = float(items[2])
    logging.info(f'received {x1}, {y1}, {x2}, {y2}')
    xx = complex(x1, x2)
    yy = complex(y1, y2)
    logging.info(f'received {xx}, {yy}')
    await update.message.reply_text(f'{xx} + {yy} = {xx + yy}')
    logging.info(f'result {xx + yy}')

async def comSub_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('complex menu item selected sub')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[1])
    y2 = float(items[2])
    logging.info(f'received {x1}, {y1}, {x2}, {y2}')
    xx = complex(x1, x2)
    yy = complex(y1, y2)
    logging.info(f'received {xx}, {yy}')
    await update.message.reply_text(f'{xx} - {yy} = {xx - yy}')
    logging.info(f'result {xx - yy}')

async def comMul_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('complex menu item selected mul')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[1])
    y2 = float(items[2])
    logging.info(f'received {x1}, {y1}, {x2}, {y2}')
    xx = complex(x1, x2)
    yy = complex(y1, y2)
    logging.info(f'received {xx}, {yy}')
    await update.message.reply_text(f'{xx} * {yy} = {xx * yy}')
    logging.info(f'result {xx * yy}')

async def comDiv_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info('complex menu item selected div')
    msg = update.message.text
    print(msg)
    items = msg.split()
    x1 = float(items[1])
    y1 = float(items[2])
    x2 = float(items[1])
    y2 = float(items[2])
    logging.info(f'received {x1}, {y1}, {x2}, {y2}')
    xx = complex(x1, x2)
    yy = complex(y1, y2)
    logging.info(f'received {xx}, {yy}')
    await update.message.reply_text(f'{xx} / {yy} = {xx / yy}')
    logging.info(f'result {xx / yy}')