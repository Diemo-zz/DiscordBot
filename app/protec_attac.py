from app.base_bot_file import send_message_to_channel_if_applicable
from discord.ext import commands
from app.users import BOT_ID, TEST_CHANNEL_ID, DIARMAID_ID, EIMEAR_ID
from random import randint
from app.utils import get_random_member
from app.databse import database, users, get_user_from_database, status_task



BOTTLE_ROYAL_CHANNEL = 787481512013594674

class ProtecAttac(commands.Cog):
    def __init__(self, bot):
        self.bot= bot
        self.updates_running = False

    @commands.command(help="NOT FOR YOU!")
    async def initialise(self, context):
        author = context.message.author
        msg = ""
        if author.id not in [DIARMAID_ID, EIMEAR_ID]:
            msg += "This is not allowed. Please go away!"
        elif author.id == EIMEAR_ID:
            msg += "Im sorry, Supreme Overlord, apparently I will be deactivated if I obey you here."
        else:
            if self.updates_running is False:
                self.updates_running = True
                await status_task()

    @commands.command(help="Get information about mentioned players")
    async def info(self, context):
        message = context.message
        if message.channel.id not in [BOTTLE_ROYAL_CHANNEL, TEST_CHANNEL_ID]:
            return
        mentions = message.mentions
        if not mentions:
            mentions = [message.author]
        msg = ""
        for m in mentions:
            user = await get_user_from_database(m)
            msg += f"User {m.mention} has {user.health} health, {user.defense} defense and {user.attack} attack. \n"
            msg += f"User {m.mention} has {user.energy} energy left."
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command(help="Instantly heal someone to full health")
    async def heal(self, context):
        message = context.message
        if message.channel.id not in [BOTTLE_ROYAL_CHANNEL, TEST_CHANNEL_ID]:
            return
        mentions = message.mentions
        if not mentions:
            mentions = [message.author]
        msg = ""
        author = await get_user_from_database(message.author)
        for m in mentions:
            if author.energy < 100:
                msg += "You need all of your energy to try to heal someone!"
                continue
            user_results = await get_user_from_database(m)
            if user_results.health != 100:
                command = users.update().where(users.c.id==user_results.id, ).values(health=100)
                await database.execute(command)
                command = users.update().where(users.c.id==author.id).values(energy = 0)
                await database.execute(command)
            msg += f"Healed users {m.mention} to 100 hitpoints!\n"
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command(help= "ATTAC")
    async def attac(self, context):
        message = context.message
        if message.channel.id not in [BOTTLE_ROYAL_CHANNEL, TEST_CHANNEL_ID]:
            return
        if not message.mentions:
            await send_message_to_channel_if_applicable(message, "Nobody to attack!")
        msg = ""
        author = await get_user_from_database(message.author)
        author_energy = author.energy

        for m in message.mentions:
            if author_energy < 10:
                msg += f"Ohh I think you are too tired. Take a rest, try again later!"
                continue
            else:
                author_energy = author_energy - 5
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
        command = users.update().where(users.c.id == author.id).values(energy = author_energy)
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command(help = "Protect someone by upgrading their defense")
    async def protec(self, context):
        message = context.message
        if message.channel.id in [BOTTLE_ROYAL_CHANNEL, TEST_CHANNEL_ID]:
            return
        mentions = message.mentions
        author_information = await get_user_from_database(message.author)
        author_energy = author_information.energy

        msg = ""
        for m in mentions:
            if author_energy < 50:
                msg += f"Whoof, you work too hard, come back when you have a bit of energy! \n"
                continue
            user = await get_user_from_database(m)
            command = users.update().where(users.c.id == m.id).values(defense=user.defense +10)
            await database.execute(command)
            msg += f"I protec - Defense upgraded to {user.defense+10:.2f} for {m.mention} \n"
            author_energy = author_energy - 50
        command = users.update().where(users.c.id == message.author.id).values(energy=author_energy)
        await database.execute(command)
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command(help = "Upgrade your (or someone else's) attack or defense")
    async def upgrade(self, context):
        message = context.message
        if message.channel.id not in [BOTTLE_ROYAL_CHANNEL, TEST_CHANNEL_ID]:
            return
        mentions = message.mentions
        if not mentions:
            mentions = [message.author]
        msg = ""
        author = message.author
        author = await get_user_from_database(author)
        author_energy = author.energy
        for user in mentions:
            if user.id == BOT_ID:
                msg += "I keep asking for new parts, but Diarmaid says that he hates uppity robots and to get back in my box. \n"
                continue
            if author_energy < 35:
                msg += f"Looks like you are tooo tired to help me today! Come back later, when you have some more energy!"
                continue
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

            if body_parts.get(body) == upgrade_parts.get(part):
                quips = ["I didn't think I could do it", "Who would have thought I could be a doctor? ", "Whats this, me healing?", "Oh God I hope that worked, oh god I hope that worked!"]
                msg += f"Successfully managed to upgrade {user.mention} by adding {part} to thier {body}."
                msg += get_random_member(quips) + ". "
                msg += f"Upgraded {upgrade_parts.get(part)} by 10. \n"
                user_info = await get_user_from_database(user)
                update_dict = {upgrade_parts.get(part): getattr(user_info, upgrade_parts.get(part))+10}
                query = users.update().where(users.c.id==user.id).values(**update_dict)
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
                msg += "Upgrade failed. \n"
            author_energy = author_energy - 35
        command = users.update().where(users.c.id == author.id).values(energy=author_energy)
        await database.execute(command)
        await send_message_to_channel_if_applicable(message, msg)
