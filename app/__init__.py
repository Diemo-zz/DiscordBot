from app.base_bot_file import bot
import app.compliments
import app.insults
import app.story
import app.protec_attac
import app.statistisc
import app.thatswhatshesaid
import app.thatswhatshesaid
import app.apod
from app.sayings import Sayings
from app.protec_attac import ProtecAttac

bot.add_cog(ProtecAttac(bot))
bot.add_cog(Sayings(bot))





