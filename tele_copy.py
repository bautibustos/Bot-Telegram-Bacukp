from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup 
from telegram.ext import Application,Updater, CommandHandler, JobQueue, ContextTypes, CallbackContext
import time, asyncio
import ConvertZip as Zip

#mi id 5515915265

with open("Utilidad\\token.txt", "r") as archivo:
    token = str(archivo.read())

async def hello(update: Updater, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        Zip.zipeo()
        with open("Utilidad\\name.txt", "r") as archivo:
            FileName = str(archivo.read())

        await update.message.reply_text(f'Wuachin aca tene lo tusho {update.effective_user.first_name}')
        await context.bot.send_document(chat_id=5515915265, document=open(f"MomentoZIp\\{FileName}", "rb"))
    except:
        print('Tranquilo ya salio')


def main():
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler('start', hello))

    print("coshiendo")
    # Comienza el bot
    application.run_polling()
    # Lo deja a la escucha. Evita que se detenga.


main()
