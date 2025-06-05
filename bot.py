from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

INSTRUCTION_TEXT = (
    "Петя говорит:\n"
    "1. Возьми шуруповёрт.\n"
    "2. Вруби его на максимум.\n"
    "3. Шуруп — в дерево.\n"
    "4. Если сломался — повтори пункт 1."
)

async def instruction(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(INSTRUCTION_TEXT)


def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN")
    if not token:
        raise RuntimeError("Please set the TELEGRAM_TOKEN environment variable")

    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler("инструкция", instruction))

    application.run_polling()


if __name__ == "__main__":
    main()
