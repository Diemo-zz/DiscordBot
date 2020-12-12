from app.base_bot_file import bot
import app.compliments
import app.insults
import app.statistisc
from app.sayings import Sayings
from app.protec_attac import ProtecAttac
from app.Entertainment import Entertainment

bot.add_cog(Entertainment(bot))
bot.add_cog(ProtecAttac(bot))
bot.add_cog(Sayings(bot))





