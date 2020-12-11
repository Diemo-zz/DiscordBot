from app.base_bot_file import bot, send_message_if_applicable


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

@bot.command(help="ATTAC")
async def attac(ctx):
    message = await get_attac_message(ctx.message)
    await send_message_if_applicable(ctx, message)

@bot.command(help="PROTEC")
async def protec(ctx):
    message = await get_protec_message(ctx.message)
    await send_message_if_applicable(ctx, message)