from app.base_bot_file import bot, send_message_if_applicable, get_bad_posts, get_authors
from app.users import BOT_ID, COUNT_TO_A_MILLION_ID, TEST_CHANNEL_ID
from discord.ext import commands
from discord import Embed
import validators

class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get a list of statistics about who has posted in this channel")
    async def statistics(self, ctx):
        channel = ctx.message.channel
        messages = await ctx.message.channel.history(limit=1e6).flatten()
        non_bot_messages = list(filter(lambda x: x.author.id != BOT_ID, messages))
        msg = f"There have been {len(messages)} total messages sent in this channel (including me). \n"
        msg += f"There have been {len(non_bot_messages)} non-bot messages in the channel. \n"
        msg += await count_posts(non_bot_messages)
        if ctx.message.channel.id in [COUNT_TO_A_MILLION_ID, TEST_CHANNEL_ID]:
            bad_posts = await get_bad_posts(non_bot_messages)
            msg += f"There have been {bad_posts} gifs posted to date in this channel. \n \n"
            msg += f"Disclaimer: I assume all posts which don't contain an integer are gifs, that should be good enough for this bullshit."
            last_message_time = messages[0].created_at
            first_message_time = messages[-1].created_at
            total_time_in_days = (last_message_time - first_message_time).days
            time_to_1_million = total_time_in_days*1e6/len(messages)
            msg += f"At this rate, it will take {int(time_to_1_million)} days (approx {time_to_1_million/30:0.2f} months or {time_to_1_million/365:.2f} years). \n"

            count = 0
            wrong_number = {}
            for m in reversed(messages):
                if validators.url(m.content):
                    continue
                content = m.content.split()
                found = False
                for c in content:
                    try:
                        i = int(c)
                        if i == count:
                            found = True
                            break
                    except:
                        continue
                if not found:
                    author = m.author
                    wrong_number.setdefault(author, []).append(m)
                count += 1
            for author, bm in wrong_number.items():
                msg += f"You have {len(bm)} bad messages {author.mention}. These have been send to you in a private message."
                embedVar = Embed(title=f"BAD Messages {channel.name}", description="Desc", color=0x00ff00)
                for index, message in enumerate(bm):
                    author_message = f"Find the message [here]({message.jump_url}) "
                    embedVar.add_field(name=f"Message {index}", value=author_message, inline=True)
                    if len(embedVar) > 5000:
                        await author.send(embed=embedVar)
                        embedVar = Embed(title=f"BAD Messages {channel.name} continued", description="Desc", color=0x00ff00)
                try:
                    await author.send(embed=embedVar)
                except Exception as e:
                    print(e)
                    pass

        await send_message_if_applicable(ctx, msg)


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


