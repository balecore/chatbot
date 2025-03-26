# chatbot 🤖💂‍♂️

A conversational Telegram-like bot for Bale Messenger that collects user information through a simple interactive flow.

## Features ✨
- **Stateful conversation** using Bale's user state management
- **Input validation** for age (1-100)
- **Emoji-enhanced** user interface
- **Simple architecture** easy to extend

## Code Structure 🏗️
```python
from balecore import MainBot, Filters
import asyncio

bot = MainBot(Token="YOUR_TOKEN_HERE", url="https://tapi.bale.ai")

@bot.Message(bot.filters.command("start") & bot.filters.private())
async def start(bot, update, full_update, message, User=None, File=None):
    # ... (see full code above)
