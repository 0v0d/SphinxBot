import os

import discord
from dotenv import load_dotenv

from Keep_Alive import keep_alive
from cog.Decorate import DecorateText
from cog.Random import Random
from cog.Calculation import Calculator
from cog.Weather import Weather
from cog.Weather_JP import Weather_JP
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
bot.add_cog(Weather_JP(bot))
keep_alive()
load_dotenv()
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
