from app import bot
from app.base_bot_file import send_message_to_channel_if_applicable, send_message_if_applicable
from bs4 import BeautifulSoup
import urllib.request
import re
from discord.ext import commands

from app.compliments import get_compliment
from app.insults import get_insult_message
from app.story import tell_me_a_story

base_url = "https://apod.nasa.gov/apod/"
from app.utils import get_random_member

LINK_FILE_PATH = "/app/APODImages/image_links.txt"
def get_list_of_apod_urls():
    response = urllib.request.urlopen("https://apod.nasa.gov/apod/archivepixFull.html")
    soup = BeautifulSoup(response)
    links = soup.findAll('a', attrs={'href': re.compile("^ap.*\.html$")})
    l = links[0]
    href = l.get('href')
    with open(LINK_FILE_PATH, "a") as link_file:
        for link in links:
            try:
                href = base_url + link.get('href')
                new_page = urllib.request.urlopen(href)
                s2 = BeautifulSoup(new_page)
                images = s2.findAll('a', attrs={'href': re.compile(".*jpg$")})
                for num, image in enumerate(images):
                    image_href = image.get('href')
                    file_path = image_href.replace("/", "-")
                    new_url = base_url + image_href
                    image2 = urllib.request.urlopen(new_url)
                    link_file.write(new_url+ "\n")
                    #with open("APODImages/" + file_path, "wb") as f:
                    #    f.write(image2.read())
            except:
                print("EXCEPTION OCCURRED")
                pass


class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Display a pretty picture of SPACE! *Actual space not guaranteed")
    async def apod(self, context):
        message = context.message
        with open(LINK_FILE_PATH, "r") as f:
            links = f.readlines()
        link = get_random_member(links)
        await send_message_to_channel_if_applicable(message, link)

    @commands.command(help="Let me tell you a interesting and cool story!")
    async def story(self, context):
        message = context.message
        msg = await tell_me_a_story(message)
        await send_message_to_channel_if_applicable(message, msg)


    @commands.command(help="Get me to insult people!")
    async def insult(self, context):
        message = context.message
        users_to_insult = message.mentions
        msg = ""
        for user in users_to_insult:
            insult_message = await get_insult_message(user, message)
            msg += insult_message
        await send_message_to_channel_if_applicable(message, msg)

    @commands.command(help="Tell me to compliment the selected user")
    async def compliment(self, context):
        message = context.message
        users_to_compliment = message.mentions
        msg = ""
        for user in users_to_compliment:
            compliment = await get_compliment(user)
            msg += compliment + "\n"
        await send_message_to_channel_if_applicable(message, msg)


if __name__ == "__main__":
    get_list_of_apod_urls()

