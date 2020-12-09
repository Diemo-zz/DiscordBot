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