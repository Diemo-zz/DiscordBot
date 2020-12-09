import discord
import datetime
import os

from users import COUNT_TO_A_MILLION_ID, TEST_CHANNEL_ID
from protec_attac import get_protec_message, get_attac_message

from insults import get_insult_message
from compliments import get_compliment

token = os.environ["DISCORD_BOT_TOKEN"]

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        print("MESSAGE IS FROM ME")
        return
    msg = ""
    if "!statistics" in message.content:
        messages = await message.channel.history(limit=1000000).flatten()
        non_bot_messages = list(filter(lambda x: x.author != client.user, messages))
        msg = f"There have been {len(messages)} total messages sent in this channel (including me). \n"
        msg += f"There have been {len(non_bot_messages)} non-bot messages in the channel. \n"
        msg += await count_posts(non_bot_messages)
    if "!insult" in message.content:
        users_to_insult = message.mentions
        msg = ""
        for user in users_to_insult:
            insult_message = await get_insult_message(user, message)
            msg += insult_message
    if "!compliment" in message.content:
        users_to_compliment = message.mentions
        msg = ""
        for user in users_to_compliment:
            compliment = await get_compliment(user)
            msg += compliment + "\n"
    if "!protec" in message.content:
        msg += await get_protec_message(message)
    if "!attac" in message.content:
        msg += await get_attac_message(message)
    if "!upgrade" in message.content and client.user in message.mentions:
        msg = "I keep asking for new parts, but Diarmaid says I was built on a shoestring budget and all he has left is loafers. \n \n I know, he thinks he is funny!"
    if message.channel.id in [COUNT_TO_A_MILLION_ID]:
        messages = await message.channel.history(limit=1000).flatten()
        messages = list(filter(lambda x: x.author == client.user, messages))
        my_last_message = messages[-1]
        current_time = datetime.datetime.now()
        my_last_message_time = my_last_message.created_at
        time_difference = my_last_message_time - current_time
        if time_difference.days < 1:
            return
        bad_posts = await get_bad_posts(non_bot_messages)
        msg += f"There have been {bad_posts} gifs posted to date in this channel. \n \n"
        msg += f"Disclaimer: I assume all posts which don't contain an integer are gifs, I am sure that Diarmaid will get around to programming something better soon."
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
    if msg:
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
