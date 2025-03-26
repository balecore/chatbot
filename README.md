# chatbot 🤖💂‍♂️

A conversational Telegram-like bot for Bale Messenger that collects user information through a simple interactive flow.

## Features ✨
- **Stateful conversation** using Bale's user state management
- **Input validation** for age (1-100)
- **Emoji-enhanced** user interface
- **Simple architecture** easy to extend

## Code Structure 🏗️
```python
from balecore import MainBot
import asyncio

bot = MainBot(Token="YOUR_TOKEN_HERE", url="https://tapi.bale.ai")

@bot.Message(bot.filters.command("start") & bot.filters.private())
async def start(bot, update, full_update, message, User=None, File=None):
    bot.set_user_state(message.from_user.id, "name")
    await bot.send_message(message.chat.id, "👋 Hello! Please tell me your name:")

@bot.Message(bot.filters.private() & bot.filters.text())
async def handle_input(bot, update, full_update, message, User=None, File=None):
    state = bot.get_user_state(message.from_user.id)
    if state == "name":
        bot.set_user_state(message.from_user.id, "age")
        await bot.send_message(message.chat.id, f"✨ Hi {message.text}!\nPlease enter your age:")
    elif state == "age":
        if message.text.isdigit() and 0 < int(message.text) <= 100:
            await bot.send_message(message.chat.id, "✅ Thank you!\nType /start to begin again")
            bot.clear_user_state(message.from_user.id)
        else:
            await bot.send_message(message.chat.id, "⚠️ Please enter a valid age (1-100)")

asyncio.run(bot.start())
