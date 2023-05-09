import os

import discord
from dotenv import load_dotenv
from discord.ext import commands


from cog.Random import Random
from cog.Calculation import Calculator


bot = discord.Bot()


@bot.slash_command()
async def hello(ctx, name: str = None):
    name = name or ctx.author.name
    await ctx.respond(f"Hello {name}!")


@bot.user_command(name="Say Hello")
async def hi(ctx, user):
    await ctx.respond(f"{ctx.author.mention} says hello to {user.name}!")

@bot.event
async def on_ready():
    print("起動完了")
    print(bot.user.name)  # Botの名前
    print(bot.user.id)  # ID
    await bot.change_presence(activity=discord.Game(
        name="im sleepy"))


bot.add_cog(Random(bot))
bot.add_cog(Calculator(bot))
load_dotenv()
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
