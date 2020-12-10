import discord
import datetime
import os

import statistisc
import users
import story
import upgrade
import protec_attac
import insults
import compliments
from base_bot_file import bot

token = os.environ["DISCORD_BOT_TOKEN"]

bot.run(token)
