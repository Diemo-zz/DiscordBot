from app.base_bot_file import bot
from app.Entertainment import Entertainment
from app.RoleInteractions import RolesMaster

bot.add_cog(RolesMaster(bot))
bot.add_cog(Entertainment(bot))
