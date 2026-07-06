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


if __name__ == "__main__":
    iniciar_bot(executar)
