import os

from app import bot

token = os.environ["DISCORD_BOT_TOKEN"]

bot.run(token)
