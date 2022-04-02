from discord.ext import commands
from discord.utils import get
from typing import List
import emoji
import regex
import random

BOT_ID = 771058009454411857
def get_random_member(list_in: List):
    if len(list_in) > 0:
        return list_in[int(random.random() * len(list_in))]
    else:
        return None

def find_emojis(text):
    emoji_list = []
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            emoji_list.append(word)
    return emoji_list


class RolesMaster(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.watched_message_id = 0
        self.message = "Generic Message"
        self.roles = {'MEE6': '🧪', "test": "🚙"}

    @commands.command(help="Print Roles")
    @commands.has_role("Admin")
    async def print_roles(self, context):
        guild = context.message.guild
        roles = [r.name for r in guild.roles]
        await context.message.channel.send(f"Roles are: {roles}")

    @commands.command()
    @commands.has_role("Admin")
    async def ar(self, context):
        message = context.message
        emojis = find_emojis(message.content)
        if len(emojis) != 1:
            await message.channel.send("Unable to recognise Emoji")
            return
        words = message.content.split(" ")
        words = [w for w in words if w not in emojis + ["!ar"]]
        if len(words) != 1:
            await message.channel.send("Unable to recognise role")
            return
        role = words[0]
        emoji_to_set = emojis[0]
        roles = message.guild.roles
        role_names = [r.name for r in roles]
        if role not in role_names:
            await message.guild.create_role(name=role)
        self.roles[role] = emoji_to_set
        await message.channel.send(f"Associated role {role} with emoji {emoji_to_set}")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.message.id != self.watched_message_id or user.id == BOT_ID:
            return
        for k, v in self.roles.items():
            if v == str(reaction):
                user_roles = user.roles
                if k not in user_roles:
                    role = get(user.guild.roles, name=k)
                    await user.add_roles(role, reason="Clicked emoji")

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if reaction.message.id != self.watched_message_id:
            return
        user_roles = [r.name for r in user.roles]
        for k, v in self.roles.items():
            if str(reaction) == v:
                if k in user_roles:
                    role = get(user.guild.roles, name=k)
                    await user.remove_roles(role)

    @commands.command()
    @commands.has_role("Admin")
    async def set_message(self, context):
        message = context.message.content.lstrip("!set_message").strip()
        self.message = message

    @commands.command()
    async def initialise_roles(self, context):
        channel = context.message.channel
        guild = context.message.guild
        if self.watched_message_id:
            msg = await channel.fetch_message(self.watched_message_id)
            await msg.delete()

        all_roles = [r.name for r in guild.roles]
        unknown_roles = list(set(all_roles) - set(self.roles.keys()))
        for role in unknown_roles:
            random_emoji = get_random_member(list(emoji.UNICODE_EMOJI['en'].keys()))
            self.roles[role] = random_emoji
        message = self.message + "\n \n"
        for role, symbol in self.roles.items():
            message += f"{role}: {symbol}\n"
        test = await channel.send(message)
        self.watched_message_id = test.id

        for role_name, role_emoji in self.roles.items():
            await test.add_reaction(role_emoji)

    @commands.command()
    @commands.has_role("Admin")
    async def delete_roles(self, context):
        message_content = context.message.content
        message_content = message_content.lstrip("!delete_roles").strip()
        roles = message_content.split(" ")
        for role in roles:
            guild_role = get(context.message.guild.roles, name=role)
            if role in self.roles:
                del self.roles[role]
            await guild_role.delete()





