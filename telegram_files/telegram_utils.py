from telegram import Bot


async def send_telegram_message(bot_token, admin_chat_id, message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=admin_chat_id, text=message)

