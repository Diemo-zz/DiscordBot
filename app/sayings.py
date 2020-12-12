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
        should_respond = await self.should_say_thats_what_she_said(message.content)
        if should_respond:
            await send_message_to_channel_if_applicable(message, "That's what she said")

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

