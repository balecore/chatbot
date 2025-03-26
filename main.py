from balecore import MainBot
import asyncio

# 🤖 Initialize bot with token and API URL
bot = MainBot(Token="YOUR_TOKEN_HERE", url="https://tapi.bale.ai")

# 🎯 Start command handler
@bot.Message(bot.filters.command("start") & bot.filters.private())
async def start(bot, update, full_update, message, User=None, File=None):
    bot.set_user_state(message.from_user.id, "name")
    await bot.send_message(message.chat.id, "👋 Hello! Please tell me your name:")

# ✉️ Message handler for user inputs
@bot.Message(bot.filters.private() & bot.filters.text())
async def handle_input(bot, update, full_update, message, User=None, File=None):
    state = bot.get_user_state(message.from_user.id)
    
    # 📛 Name state
    if state == "name":
        bot.set_user_state(message.from_user.id, "age")
        await bot.send_message(message.chat.id, f"✨ Hi {message.text}!\nPlease enter your age:")
    
    # 🔢 Age state
    elif state == "age":
        if message.text.isdigit() and 0 < int(message.text) <= 100:
            await bot.send_message(message.chat.id, "✅ Thank you!\nType /start to begin again")
            bot.clear_user_state(message.from_user.id)
        else:
            await bot.send_message(message.chat.id, "⚠️ Please enter a valid age (1-100)")

# 🚀 Start the bot
asyncio.run(bot.start())
