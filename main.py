from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    MessageHandler,
    filters,
)

from config import TOKEN
from supervisor import iniciar_bot
from worker import processar_mensagem

async def processar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not update.message:
        return

    await processar_mensagem(update.message)


def executar():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        MessageHandler(
            filters.ALL,
            processar,
        )
    )

    print("=" * 40)
    print("☠ APAGADOR 3000 V3 ONLINE")
    print("=" * 40)

    app.run_polling(
        drop_pending_updates=True
    )

from flask import Flask
import threading
import os

web = Flask(__name__)

@web.route("/")
def home():
    return "Bot online!"

def servidor():
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

threading.Thread(target=servidor, daemon=True).start()
if __name__ == "__main__":
    iniciar_bot(executar)
