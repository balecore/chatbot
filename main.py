from balecore import MainBot, Filters
import asyncio

bot = MainBot(Token="", url="https://tapi.bale.ai")

@bot.Message(bot.filters.command("start") & bot.filters.private())
async def start(bot, update, full_update, message, User=None, File=None):
    bot.set_user_state(message.from_user.id, "name")
    await bot.send_message(message.chat.id, "سلام! نام خود را بگویید:")

@bot.Message(bot.filters.private() & bot.filters.text())
async def handle_input(bot, update, full_update, message, User=None, File=None):
    state = bot.get_user_state(message.from_user.id)
    if state == "name":
        bot.set_user_state(message.from_user.id, "age")
        await bot.send_message(message.chat.id, f"سلام {message.text}!\nسن خود را بگویید:")
    elif state == "age":
        if message.text.isdigit() and 0 < int(message.text) <= 100:
            await bot.send_message(message.chat.id, "ممنون از آشنایی! /start برای شروع مجدد")
            bot.clear_user_state(message.from_user.id)
        else:
            await bot.send_message(message.chat.id, "لطفاً سن معتبر وارد کنید (1-100)")

asyncio.run(bot.start())
