import discord
import datetime
import os
token = os.environ["DISCORD_BOT_TOKEN"]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if "!statistics" in message.content:
        messages = await message.channel.history(limit=1000000).flatten()
        msg = f"There have been {len(messages)} total messages sent in this channel (including me). \n"
        non_bot_messages = list(filter(lambda x: x.author != client.user, messages))
        msg += f"There have been {len(non_bot_messages)} non-bot messages in the channel. \n"
        msg += await count_posts(non_bot_messages)
        if message.channel.id in [785962469579423845, 763510316290015322]: # test channel, count to a milliion channel
            bad_posts = await get_bad_posts(non_bot_messages)
            msg += f"There have been {bad_posts} posts which do not contain an integer posted in this channel. - Likely gifs, because I can't handle them."
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
                return
        await message.channel.send(msg)

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

async def get_authors(messages):
    authors = {}
    for m in messages:
        authors[m.author] = authors.get(m.author, 0) + 1
    return authors

async def count_posts(non_bot_messages):
    authors = get_authors(non_bot_messages)
    first_message = non_bot_messages[-1]
    last_message = non_bot_messages[0]
    number_of_messages = len(non_bot_messages)
    authors = await authors
    msg = ""
    msg += f"The first message was sent on {first_message.created_at} and the last message was sent on {last_message.created_at}. \n"
    msg += f"There have been an average of {int(number_of_messages / max(1, (last_message.created_at - first_message.created_at).days))} messages per day. \n"
    msg += f"There have been {len(authors)} specific users in the channel, and they have posted: \n"
    max_messages = 0
    max_auth = None
    for author, value in authors.items():
        if value > max_messages:
            max_auth = author
            max_messages = value
        msg += f"{author.name}: {value} \n"
    msg += f"The user with the most messages is {max_auth.name} with {max_messages} messages."
    return msg


client.run(token)
