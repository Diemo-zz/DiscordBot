from discord.ext import commands
from app.users import BOT_ID
from app.base_bot_file import send_message_to_channel_if_applicable


class Sayings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == BOT_ID:
            return
        lower_case_contents = message.content.lower()
        if "good bot" in lower_case_contents:
            await send_message_to_channel_if_applicable(message, "Thanks")
        if "bad bot" in lower_case_contents:
            await send_message_to_channel_if_applicable(message, "I'm tring my best!")
        should_respond = await self.should_say_thats_what_she_said(message.content)
        if should_respond:
            await send_message_to_channel_if_applicable(message, "That's what she said")
        if ("harumph" in message.content.lower()) or ("harrumph" in message.content.lower()):
            await send_message_to_channel_if_applicable(message, "https://media1.giphy.com/media/xTiTnHz4LKeY7zNDvq/giphy.gif")
        if any([BOT_ID == m.id for m in message.mentions]):
            return_msg = ""
            if "i know" in lower_case_contents:
                return_msg += "You don't know anything! I'm made by a doctor you know!"
                if "please" in lower_case_contents:
                    return_msg += " I'm trying my best here, you know. I'm just a poor robot in a world where everyone hates machines.\n"
            else:
                return_msg += "Yes? "
                if "?" in lower_case_contents:
                    return_msg += "I'm to stupid to understand how to answer questions. "
                if "please" in lower_case_contents:
                    return_msg += "You are so polite to me! "
                if "sorry" in lower_case_contents:
                    return_msg += "Apology accepted. Now lets forget this ever happened!"
            await send_message_to_channel_if_applicable(message, return_msg)

    async def should_say_thats_what_she_said(self, message_contents):
        message_contents = message_contents.lower()
        sayings = ["really big", "so small", "was disappointing", "super unsatisfying", "soooooo good", "sooooooo goood"]
        if any([i in message_contents for i in sayings]):
            return True
        else:
            return False

    @commands.command(help="That's what she said")
    async def thatswhatshesaid(self, message):
        msg = "Thats's what she said"
        await message.channel.send(msg)

    @commands.command(help="No explanation needed - tell me what you want me to suck")
    async def suck(self, message):
        msg = f"Fuck off {message.author.mention}, I aint sucking shit!"
        await send_message_to_channel_if_applicable(message.channel, msg)

    @commands.command(help="alias for suck")
    async def suckmadick(self, message):
        await self.suck(message)

