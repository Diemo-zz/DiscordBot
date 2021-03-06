import datetime

from discord.ext import commands
from discord import Embed, Intents

from app.users import COUNT_TO_A_MILLION_ID, TEST_CHANNEL_ID, BOT_ID

bot = commands.Bot(command_prefix="!", case_insensitive=True,  intents=Intents.all())


async def send_message_if_applicable(ctx, msg):
    if not msg:
        return
    message = ctx.message
    messages_to_send = [msg[i:i+2000] for i in range(0, len(msg), 2000)]
    for m in messages_to_send:
        await send_message_to_channel_if_applicable(message, m)

async def send_message_to_channel_if_applicable(message, msg, embed=False):
    channel = message.channel
    if channel.id in [COUNT_TO_A_MILLION_ID]:
        messages = await channel.history(limit=1000).flatten()
        messages = list(filter(lambda x: x.author.id == BOT_ID, messages))
        if messages:
            my_last_message = messages[0]
            current_time = datetime.datetime.now()
            my_last_message_time = my_last_message.created_at
            time_difference = current_time - my_last_message_time
            if time_difference.days < 1:
                return

        split_message = message.content.split()
        last_integer = None
        for c in split_message:
            try:
                x = int(c)
                last_integer = x
            except:
                pass
        if last_integer is not None:
            msg = f"The next number is: {last_integer + 1} \n" + msg
        else:
            msg = ""
    if msg:
        if embed:
            embedVar = Embed(title="Bot Message", description="A friendly message from your BOT", color=0x00ff00)
            embedVar.add_field(name="Information", value=msg, inline=False)
            await channel.send(embed=embedVar)
        else:
            await channel.send(msg)


async def get_bad_posts(messages):
    bad_posts = 0
    for m in messages:
        contents = m.content.split()
        contains_integer = False
        for c in contents:
            try:
                int(c)
                contains_integer = True
            except:
                pass
        if not contains_integer:
            bad_posts += 1
    return bad_posts


async def contains_integer(message_content):
    contents = message_content.split()
    contains_integer = False
    for c in contents:
        try:
            i = int(c)
            contains_integer = True
            break
        except:
            pass
    if contains_integer:
        return i
    else:
        return None


async def get_authors(messages):
    authors = {}
    for m in messages:
        authors[m.author] = authors.get(m.author, 0) + 1
    return authors