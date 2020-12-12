from app.base_bot_file import bot
from app.sayings import Sayings
from app.protec_attac import ProtecAttac
from app.Entertainment import Entertainment
from app.statistisc import Information

bot.add_cog(Information(bot))
bot.add_cog(Entertainment(bot))
bot.add_cog(ProtecAttac(bot))
bot.add_cog(Sayings(bot))





