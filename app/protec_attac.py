from app.base_bot_file import send_message_to_channel_if_applicable
from discord.ext import commands
from app.users import BOT_ID,EIMEAR_ID
from random import randint

class ProtecAttac(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.command()
    async def attac(self, message):
        m = await get_attac_message(message)
        await send_message_to_channel_if_applicable(message.channel, m)

    @commands.command()
    async def protec(self, message):
        m = await get_protec_message(message)
        await send_message_to_channel_if_applicable(message.channel, m)

    @commands.command()
    async def upgrade(self, message):
        mentions = message.mentions
        if not mentions:
            msg = f"""Who do you want me to upgrade? Make sure to mention them like this, {message.author.mention}."""
        else:
            if any([m.id == BOT_ID for m in mentions]):
                msg = "I keep asking for new parts, but Diarmaid says I was built on a shoestring budget and all he has left is loafers. \n \n I know, he thinks he is funny!"
            else:
                msg = ""
                for user in mentions:
                    if user.id == EIMEAR_ID:
                        msg += "I can't upgrade the Supreme Overlord"
                    else:
                        upgrade_types = ["armour", "health", "defense", "speed", "charisma"]
                        upgrade_object = ["a new heart", "a new shield", "a new consience", "a new face", "a new leg", "a repurposed radioactivce hand", "a giant robot",
                                      "some cute puppies"]
                        msg += f"Attempting to upgrade user {user.mention}: selecting part \n"
                        msg += f"Attempting to upgrade their {get_random_member(upgrade_types)} by adding {get_random_member(upgrade_object)} \n"
                        msg += f"\n \n Buzzzz Whiirrrr Buzzz \n \n"
                        if randint(0, 100) < 75:
                            msg += f"I don't think there should be so much blood. Oh well, please try again later, provided you still have limbs left. \n"
                        else:
                            msg += "Upgrade successful. I do hope you feel better. \n"
        await send_message_to_channel_if_applicable(message.channel, msg)

async def get_protec_message(message):
    mentioned_users = message.mentions
    if mentioned_users:
        msg = ""
        for user in mentioned_users:
            msg += f"KEINE SORGE {user.mention}, I PROTEC U"
    else:
        msg = "I PROTEC \n"
    return msg

async def get_attac_message(message):
    mentioned_users = message.mentions
    if mentioned_users:
        msg = ""
        for user in mentioned_users:
            msg += f"VIELE SORGE {user.mention}, I ATTAC"
    else:
        msg = "I ATTAC \n"
    return msg

#@bot.command(help="ATTAC")
#async def attac(ctx):
#    message = await get_attac_message(ctx.message)
#    await send_message_if_applicable(ctx, message)

#@bot.command(help="PROTEC")
#async def protec(ctx):
#    message = await get_protec_message(ctx.message)
#    await send_message_if_applicable(ctx, message)