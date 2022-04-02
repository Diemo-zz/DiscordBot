from discord.ext import commands
from discord import Embed, Intents
from app.get_apod_images import APODImage

bot = commands.Bot(command_prefix="!", case_insensitive=True, intents=Intents.all())


async def send_message_if_applicable(ctx, msg):
    if not msg:
        return
    message = ctx.message
    messages_to_send = [msg[i : i + 2000] for i in range(0, len(msg), 2000)]
    for m in messages_to_send:
        await send_message_to_channel_if_applicable(message, m)


async def send_message_to_channel_if_applicable(message, msg, embed=False):
    channel = message.channel
    if msg:
        if embed:
            embed_var = Embed(
                title="Bot Message",
                description="A friendly message from your BOT",
                color=0x00FF00,
            )
            embed_var.add_field(name="Information", value=msg, inline=False)
            await channel.send(embed=embed_var)
        else:
            await channel.send(msg)


async def send_image(message, msg: APODImage):
    channel = message.channel
    if msg:
        cred = f"\nBy {msg.author.name} ({msg.author.email})"
        embed = Embed(title=f"{msg.title}", description=msg.description, url=msg.link)
        embed.add_field(name="Credentials", value=cred, inline=True)
        embed.set_image(url=msg.url)
        await channel.send(embed=embed)
