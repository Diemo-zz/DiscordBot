from app.base_bot_file import bot, send_message_if_applicable
from app.users import BOT_ID, EIMEAR_ID
from app.utils import get_random_member
from random import randint

@bot.command(help = "No explanation needed - just ask me what you want to suck")
async def suck(ctx):
    msg = f"Fuck off {ctx.message.author.mention}, I aint sucking shit!"
    await send_message_if_applicable(ctx, msg)

@bot.command(help="alias for suck")
async def suckmadick(ctx):
    await suck(ctx)

@bot.command(help = "Send someone to the bot to be upgraded!")
async def upgrade(ctx):
    mentions = ctx.message.mentions
    if not mentions:
        msg = f"""Who do you want me to upgrade? Make sure to mention them like this, {ctx.message.author.mention}."""
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
    await send_message_if_applicable(ctx, msg)
