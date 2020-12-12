from app.base_bot_file import bot
import app.compliments
import app.insults
import app.story
import app.protec_attac
import app.statistisc
import app.thatswhatshesaid
import app.upgrade
import app.thatswhatshesaid
import app.apod
from app.edit_message import ThatsWhatSheSaid
from app.protec_attac import ProtecAttac

bot.add_cog(ProtecAttac(bot))
bot.add_cog(ThatsWhatSheSaid(bot))





