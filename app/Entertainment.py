from typing import List
from app.base_bot_file import send_image
from discord.ext import commands
import random

from app.get_apod_images import get_apod_links


def get_random_member(list_in: List):
    if len(list_in) > 0:
        return list_in[int(random.random() * len(list_in))]
    else:
        return None


class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.image_links = get_apod_links()
        self.bot = bot

    @commands.command(
        help="Display a pretty picture of SPACE! *Actual space not guaranteed"
    )
    async def apod(self, context):
        message = context.message
        link = get_random_member(self.image_links)
        await send_image(message, link)

    @commands.command(help="Reload the images from APOD - warning can take a while!")
    async def reload(self, context):
        message = context.message
        content = message.content
        force_reload = "force" in content
        self.image_links = get_apod_links(force_reload)
