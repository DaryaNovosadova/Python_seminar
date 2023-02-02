from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *
from calc import *
from logg import logging


app = ApplicationBuilder().token("6057114702:AAFYII9jCG7X8qhPnf_f3zCg-Xww9fk_BWU").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("1", rac_command))
app.add_handler(CommandHandler("2", com_command))
app.add_handler(CommandHandler("3", sum_command))
app.add_handler(CommandHandler("4", sub_command))
app.add_handler(CommandHandler("5", mul_command))
app.add_handler(CommandHandler("6", div_command))
app.add_handler(CommandHandler("7", pow_command))
app.add_handler(CommandHandler("8", sqrt_command))
app.add_handler(CommandHandler("9", comSum_command))
app.add_handler(CommandHandler("10", comSub_command))
app.add_handler(CommandHandler("11", comMul_command))
app.add_handler(CommandHandler("12", comDiv_command))
app.add_handler(CommandHandler("13", divP_command))
app.add_handler(CommandHandler("14", divC_command))
app.add_handler(CommandHandler("15", divO_command))
app.add_handler(CommandHandler("0", hi_command))


print('server start')
logging.info('Start program')
app.run_polling()