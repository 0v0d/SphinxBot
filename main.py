import os

import discord

from Keep_Alive import keep_alive
from cog.Decorate import DecorateText
from cog.Random import Random
from cog.Calculation import Calculator
from cog.Weather import Weather

bot = discord.Bot()


@bot.event
async def on_ready():
  print("Started")
  print(bot.user.name)
  print(bot.user.id)
  await bot.change_presence(activity=discord.Game(name="im sleepy"))


bot.add_cog(Random(bot))
bot.add_cog(Calculator(bot))
bot.add_cog(Weather(bot))
bot.add_cog(DecorateText(bot))
keep_alive()
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
