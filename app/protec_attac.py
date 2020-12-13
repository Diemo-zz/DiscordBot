from app.base_bot_file import send_message_to_channel_if_applicable
from discord.ext import commands
from app.users import BOT_ID,EIMEAR_ID
from random import randint
from app.utils import get_random_member
from app.databse import database, users, get_user_from_database


class ProtecAttac(commands.Cog):
    def __init__(self, bot):
        self.bot= bot

    @commands.command()
    async def info(self, context):
        message = context.message
        mentions = message.mentions
        if not mentions:
            mentions = [message.author]
        msg = ""
        for m in mentions:
            user = await get_user_from_database(m)
            msg += f"User {m.mention} has {user.health} health, {user.defense} defense and {user.attack} attack. \n"
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command()
    async def heal(self, context):
        message = context.message
        mentions = message.mentions
        if not mentions:
            mentions = [message.author]
        msg = ""
        for m in mentions:
            user_results = await get_user_from_database(m)
            if user_results.health != 100:
                command = users.update().where(users.c.id==user_results.id, ).values(health=100)
                await database.execute(command)
            msg += f"Healed users {m.mention} to 100 hitpoints!\n"
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command()
    async def attac(self, context):
        message = context.message
        if not message.mentions:
            await send_message_to_channel_if_applicable(message.channel, "Nobody to attack!")
        msg = ""
        author = await get_user_from_database(message.author)

        for m in message.mentions:
            user_information = await get_user_from_database(m)
            my_attack = author.attack
            your_defense = author.defense
            ration = my_attack/your_defense
            amount = randint(0, 10)
            amount = amount*ration
            new_health = user_information.health - amount
            if new_health < 0:
                msg = f"Oh wow, you killed him. Bye bye {m.mention}"
                command = users.update().where(users.c.id == m.id).values(health=user_information.health - amount)
            else:
                msg += f"Attacking {m.mention} - did {amount:.2f} damage."
                msg += f"User {m.mention} now has {user_information.health-amount:.2f} health left.\n"
                command = users.update().where(users.c.id == m.id).values(health=user_information.health - amount)
            await database.execute(command)
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command()
    async def protec(self, context):
        message = context.message
        mentions = message.mentions
        msg = ""
        for m in mentions:
            user = await get_user_from_database(m)
            command = users.update().where(users.c.id == m.id).values(defense=user.defense +10)
            await database.execute(command)
            msg += f"I protec - Defense upgraded to {user.defense+10:.2f} for {m.mention} \n"
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command()
    async def upgrade(self, context):
        message = context.message
        mentions = message.mentions
        if not mentions:
            msg = f"""Who do you want me to upgrade? Make sure to mention them like this, {message.author.mention}."""
        else:
            if any([m.id == BOT_ID for m in mentions]):
                msg = "I keep asking for new parts, but Diarmaid says I was built on a shoestring budget and all he has left is loafers. \n \n I know, he thinks he is funny!"
            else:
                msg = ""
                for user in mentions:
                    upgrade_parts = {
                            "a giant robot gun": "attack",
                            "a tiny Chihuahua": "attack",
                            "medieval armour": "defense",
                            "Indiana Jones's whip": "attack",
                            "the Bob Dylan record 'Hurricane'": "defense",
                            "the worlds worst children's book": "defense"
                    }
                    body_parts ={
                        "face": "defense",
                        "torso": "defense",
                        "legs": "defense",
                        "arms": "attack",
                        "hands": "attack",
                        "toungue": "attack"
                    }
                    part = get_random_member(list(upgrade_parts.keys()))
                    body = get_random_member(list(body_parts.keys()))
                    body = "arms"
                    part = "Indiana Jones's whip"

                    if body_parts.get(body) == upgrade_parts.get(part):
                        quips = ["I didn't think I could do it", "Who would have thought I could be a doctor", "Whats this, me healing?", "Oh God I hope that worked, oh god I hope that worked!"]
                        msg += f"Successfully managed to upgrade {user.mention}."
                        msg += get_random_member(quips)
                        msg += f"Upgraded {upgrade_parts.get(part)} by 10"
                        user_info = await get_user_from_database(user)
                        update_dict = {upgrade_parts.get(part): getattr(user_info, upgrade_parts.get(part))+10 }
                        query = users.update().where(users.c.id==user.id).values(**update_dict)
                        print(query)
                        await database.execute(query)
                    else:
                        actions = [
                            "Run away, run away, run away. \n",
                            "Better help them up. \n"
                        ]
                        msg += f"Attempting to upgrade user {user.mention}: selecting part \n"
                        msg += f"Attempting to upgrade their {body} by adding {part} \n"
                        msg += f"\n \n Buzzzz Whiirrrr Buzzz \n \n"
                        msg += f"OH GOD WHY IS THERE SO MUCH BLOOD! "
                        msg += get_random_member(actions)
                        msg += "Upgrade failed"

        await send_message_to_channel_if_applicable(message, msg)

    @commands.command()
    async def bd(self, ctx):
        await database.connect()
        print("database connected")

    @commands.command()
    async def sd(self, ctx):
        await database.disconnect()

