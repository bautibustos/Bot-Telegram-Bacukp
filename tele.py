import time
import ConvertZip as Zip
from telegram import Update
from telegram.ext import Updater, CommandHandler, JobQueue

#mi id 5515915265

with open("Utilidad\\token.txt", "r") as archivo:
    token = str(archivo.read())

def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.message.reply_text(f'Wuachin aca tene lo tusho {update.effective_user.first_name}')
    Zip.zipeo()
    with open("Utilidad\\name.txt", "r") as archivo:
        FileName = str(archivo.read())
    context.bot.send_document(chat_id=5515915265, document=open(f"MomentoZIp\\{FileName}", "rb"))
    time.sleep(20)

def main():
    updater=Updater(token, use_context=True)#use_context=True
    job_queue = updater.job_queue
    updater.add_handler(CommandHandler("i", hello))
    print("coshiendo")
    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    updater.idle()
