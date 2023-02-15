from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import calculate
import write_log as wl

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def my_calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    my_text = update.message.text
    wl.write_data(f'Начало работы программы.\nПользователь ввел выражение: {my_text}')
    # await update.message.reply_text(f'Hello {update.effective_user.first_name}')
    await update.message.reply_text(calculate.calc_first(my_text))

app = ApplicationBuilder().token("6277873420:AAFnQMKtaWc1umP6iYujHazyghtl_id54J4").build()

app.add_handler(MessageHandler(filters.TEXT, my_calc))
# app.add_handler(CommandHandler("hello", hello))

app.run_polling()