from discord.ext import commands
import emoji



class MileyReaction(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 287273675168808961:
            poo = '\U0001F4A9'
            O = '\U0001F1F4'
            S = '\U0001F1F8'
            T = u"\U0001F1F9"
            P = '\U0001F17F'
            NG = '\U0001F196'
            i = emoji.emojize(":information:")
            await message.add_reaction(S)
            await message.add_reaction(T)
            await message.add_reaction(O)
            await message.add_reaction(P)
            await message.add_reaction(poo)
            await message.add_reaction(i)
            await message.add_reaction(NG)
